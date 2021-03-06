#!/usr/bin/env python3
# coding: utf-8

import sys
import datetime
import pprint
import urllib.parse
import requests  # $ pip install requests

try:
    # raise Exception("test")
    from tzlocal import get_localzone  # $ pip install tzlocal
except Exception:
    print("N.B.: Times are UTC.")

PLUTO_URL_TEMPLATE = (
    "http://api.pluto.tv/v2/channels"
    "?start={datetime_start}&stop={datetime_end}"
)
my_channel_slugs = [
    "pluto-tv-sci-fi-de",
    "pluto-tv-star-trek-de",
    "doctor-who-classic-de",
]
my_series_slugs = [
    "star-trek-discovery-de",
    "star-trek-discovery-ptv2",
    "star-trek-enterprise-de",
]


# example_urls:
# example URLs generated in https://github.com/evoactivity/PlutoIPTV
PLUTO_URL_1 = (
    "http://api.pluto.tv/v2/channels"
    "?start=2022-02-20%2023%3A00%3A00.000%2B0100"
    "&stop=2022-02-22%2023%3A00%3A00.000%2B0100"
)
PLUTO_URL = (
    "http://api.pluto.tv/v2/channels"
    "?start=2022-02-28%2020%3A00%3A00.000%2B0100"
    "&stop=2022-03-02%2020%3A00%3A00.000%2B0100"
)


def create_pluto_url(dt_start, dt_end, template=PLUTO_URL_TEMPLATE):
    params = {
        "datetime_start": urllib.parse.quote(dt_start + ".000+0100"),
        "datetime_end": urllib.parse.quote(dt_end + ".000+0100"),
    }
    url = template.format(**params)
    return url


def create_pluto_url_test(PLUTO_URL):
    # test = create_pluto_url(dt_start="2022-02-20 23:00:00",
    #                         dt_end="2022-02-22 23:00:00")
    test = create_pluto_url(
        dt_start="2022-02-28 20:00:00", dt_end="2022-03-02 20:00:00"
    )
    print(PLUTO_URL)
    print(test)
    return test == PLUTO_URL


def pluto_url_around_now_OLD(
    pastdays=0, futuredays=2, time_of_day_string="20:00:00"
):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=pastdays)
    yesterday_string = ("%s" % yesterday)[:11] + time_of_day_string
    # print(yesterday_string)
    the_day_after_tomorrow = datetime.datetime.now() + datetime.timedelta(
        days=futuredays
    )
    tdat_string = ("%s" % the_day_after_tomorrow)[:11] + time_of_day_string
    # print(tdat_string)
    url = create_pluto_url(yesterday_string, tdat_string)
    return url


def pluto_url_around_now():
    now = datetime.datetime.now()
    this_hour_string = ("%s" % now)[:13] + ":00:00"
    # print(this_hour_string)
    fortyeight_hours_later = now + datetime.timedelta(hours=48)
    f8hl_string = ("%s" % fortyeight_hours_later)[:13] + ":00:00"
    # print(f8hl_string)
    url = create_pluto_url(this_hour_string, f8hl_string)
    return url


def get_pluto_epg(url, ifprint=True):
    # url="http://api.pluto.tv/v2/channels?start=2022-02-27%2023%3A00%3A00.000%2B0100&stop=2022-03-01%2023%3A00%3A00.000%2B0100"
    # url = "http://api.pluto.tv/v3"
    try:
        pluto = requests.get(url)
    except Exception as e:
        print("PROBLEM: (%s) %s when trying to access url"
              "%s" % (type(e), e, url))
        return []

    sc = pluto.status_code
    if sc != 200:
        print("PROBLEM: request ended with status_code=%s"
              " when trying to access url:\n" % sc, url)
        return []

    j = pluto.json()
    if isinstance(j, dict) and j["statusCode"] != 200:
        pprint.pprint(j)

    elif ifprint:
        print("Success. Result list has %d elements." % len(j))

    return j


def extract_channel_slugs_only(j, titles_too=False):
    slugs = []
    for e in j:
        entry = e["slug"]
        if titles_too:
            entry += " = " + e["name"]
        slugs.append(entry)
    slugs = sorted(list(set(slugs)))
    return slugs


def print_with_newlines(j, func=extract_channel_slugs_only, titles_too=False):
    res = func(j, titles_too)
    print("\n".join(res))
    print("#############\n%d elements" % len(res))


def extract_series_slugs_only(j, titles_too=False):
    slugs = []
    for ch in j:
        timelines = ch.get("timelines", [])
        for tl in timelines:
            ep = tl["episode"]
            series = ep["series"]
            entry = series["slug"]
            if titles_too:
                entry += " = " + series["name"]
            slugs.append(entry)
    slugs = sorted(list(set(slugs)))
    return slugs


def timelines_in_channel(
    ch, print_channel_name=True, FORMATTER="(%s) %s = %d timelines"
):
    timelines = ch.get("timelines", [])
    if print_channel_name:
        print(FORMATTER % (ch["slug"], ch["name"], len(timelines)))
    return timelines


def exxsxx(ep, FORMATTER="s%02de%02d"):
    season = ep.get("season", 0)
    return FORMATTER % (season, ep["number"])


def time_info(tl):
    # to turn into localtime, this must be parsed as UTC= +0000
    start = datetime.datetime.strptime(
        tl["start"][:19] + " +0000", "%Y-%m-%dT%H:%M:%S %z"
    )
    stop = datetime.datetime.strptime(
        tl["stop"][:19] + " +0000", "%Y-%m-%dT%H:%M:%S %z"
    )
    minutes = int((stop - start).total_seconds() / 60.0)
    # turn into localtime - https://stackoverflow.com/a/1111345
    # print(start.strftime("%H:%M %b %d %Z"), end=" ...")
    if "tzlocal" in sys.modules:
        start = start.astimezone(get_localzone())

    # print(start_localtime.strftime("%H:%M %b %d %Z"))
    start_print = start.strftime("%H:%M %b %d")
    return start, start_print, minutes


def series_info(ep):
    series_name = ep["series"]["name"]
    series_slug = ep["series"]["slug"]
    return series_name, series_slug


def compile_hit(
    ep,
    start_print,
    minutes,
    series_name,
    series_slug,
    ch,
    print_each_hit=False,
    FORMATTER="%s %s '%s' %s mins '%s' [%s] %s",
):
    value = FORMATTER % (
        exxsxx(ep),
        start_print,
        ep["name"],
        minutes,
        series_name,
        series_slug,
        ch["slug"],
    )
    if print_each_hit:
        print(value)
    return value


def iterate_pluto(
    j,
    find_in_series_name=None,
    my_channel_slugs=[],
    my_series_slugs=[],
    print_channel_name=True,
    print_each_hit=False,
    print_count=True,
):

    hits, ch_slugs, series_slugs = [], [], []
    for ch in j:
        if not my_channel_slugs or ch["slug"] in my_channel_slugs:
            timelines = timelines_in_channel(ch, print_channel_name)
            for tl in timelines:
                ep = tl["episode"]
                series_name, series_slug = series_info(ep)

                if my_series_slugs and (series_slug not in my_series_slugs):
                    continue

                if find_in_series_name and (
                    find_in_series_name not in series_name
                ):
                    continue

                start, start_print, minutes = time_info(tl)
                key = (
                    ch["slug"] + "_%s" % start
                )  # unique key, only 1 thing per time on any channel?

                value = compile_hit(
                    ep,
                    start_print,
                    minutes,
                    series_name,
                    series_slug,
                    ch,
                    print_each_hit=print_each_hit,
                )

                hits.append((key, value))
                ch_slugs.append(ch["slug"])
                series_slugs.append(series_slug)
            # break
    if print_count:
        print(
            "\n#################################\n%s elements.\n" % len(hits)
        )

    result = sorted(hits, key=lambda x: x[0])
    return result, sorted(list(set(ch_slugs))), sorted(list(set(series_slugs)))


def print_result_series_channels(result, series, channels):
    if not result:
        print("EMPTY result")
    else:
        print("\n".join(list(zip(*result))[1]))
        print("Series: %s\nChannels: %s" % (series, channels))


def example_everything(j):
    # careful 2840 answers:
    result, channels, series = iterate_pluto(
        j,
        find_in_series_name=False,
        print_each_hit=False,
        print_channel_name=False,
    )
    print_result_series_channels(result, series, channels)


def example_Star_in_series_name(j):
    result, channels, series = iterate_pluto(
        j,
        find_in_series_name="Star",
        print_each_hit=False,
        print_channel_name=False,
    )
    print_result_series_channels(result, series, channels)


def example_Discovery_in_series_name(j):
    result, channels, series = iterate_pluto(
        j,
        find_in_series_name="Discovery",
        print_each_hit=False,
        print_channel_name=False,
    )
    print_result_series_channels(result, series, channels)


def example_DoctorWho_in_series_name(j):
    result, channels, series = iterate_pluto(
        j,
        find_in_series_name="Doctor Who",
        print_each_hit=False,
        print_channel_name=False,
    )
    print_result_series_channels(result, series, channels)


def example_my_channel_slugs(j, my_channel_slugs=my_channel_slugs):
    result, channels, series = iterate_pluto(
        j,
        my_channel_slugs=my_channel_slugs,
        print_each_hit=False,
        print_channel_name=False,
    )
    print_result_series_channels(result, series, channels)


def example_my_channel_slugs_and_series_slugs(
    j, my_channel_slugs=my_channel_slugs, my_series_slugs=my_series_slugs
):
    result, channels, series = iterate_pluto(
        j,
        my_channel_slugs=my_channel_slugs,
        my_series_slugs=my_series_slugs,
        print_each_hit=False,
        print_channel_name=False,
    )
    print_result_series_channels(result, series, channels)


def the_purpose_of_all_this_v1():
    url = pluto_url_around_now()
    j = get_pluto_epg(url, ifprint=False)
    result, channels, series = iterate_pluto(
        j,
        my_channel_slugs=my_channel_slugs,
        my_series_slugs=my_series_slugs,
        print_each_hit=False,
        print_channel_name=False,
        print_count=False,
    )
    print_result_series_channels(result, series, channels)


def the_purpose_of_all_this_v2(print_count=False):
    print("Find everything with 'Star Trek' in Series Name:")
    url = pluto_url_around_now()
    j = get_pluto_epg(url, ifprint=False)
    result, channels, series = iterate_pluto(
        j,
        find_in_series_name="Star Trek",
        print_each_hit=False,
        print_channel_name=False,
        print_count=print_count,
    )
    print_result_series_channels(result, series, channels)


def print_channel_slugs(titles_too=False):
    url = pluto_url_around_now()
    j = get_pluto_epg(url)
    print_with_newlines(
        j, func=extract_channel_slugs_only, titles_too=titles_too
    )


def print_series_slugs(titles_too=False):
    url = pluto_url_around_now()
    j = get_pluto_epg(url)
    print_with_newlines(
        j, func=extract_series_slugs_only, titles_too=titles_too
    )


def to_list(a_comma_b):
    my_list = a_comma_b.split(",")  # turn string into list
    return [element.strip() for element in my_list]  # remove whitespaces


def print_after_all_filters(find_in_series_name=None,
                            my_channel_slugs=None,
                            my_series_slugs=None,
                            print_count=False,
                            print_parameters=False):
    """
    any filter can be 'None' or set to include only such results
    """
    if print_parameters:
        print("find_in_series_name:", find_in_series_name)
        print("my_channel_slugs: ", my_channel_slugs)
        print("my_series_slugs:", my_series_slugs)
        print("print_count", print_count)

    channels = None if not my_channel_slugs else to_list(my_channel_slugs)
    series = None if not my_series_slugs else to_list(my_series_slugs)

    url = pluto_url_around_now()
    j = get_pluto_epg(url, ifprint=False)

    result, channels, series = iterate_pluto(
        j,
        find_in_series_name=find_in_series_name,
        my_channel_slugs=channels,
        my_series_slugs=series,
        print_each_hit=False,
        print_channel_name=False,
        print_count=print_count
    )
    print_result_series_channels(result, series, channels)

# -----------------------------------------------------------------------


def testing_all_of_the_above():
    """
    print(urllib.parse.unquote(PLUTO_URL))

    create_pluto_url_test(PLUTO_URL)
    url = pluto_url_around_now()
    print(url)
    print(PLUTO_URL == url)

    j = get_pluto_epg(url)

    print_with_newlines(j)
    print_with_newlines(j, extract_series_slugs_only)

    result, channels, series = iterate_pluto(
        j, print_channel_name=False, find_in_series_name="Star"
    )
    print_result_series_channels(result, series, channels)

    example_everything(j)
    example_Star_in_series_name(j)
    example_Discovery_in_series_name(j)
    example_DoctorWho_in_series_name(j)
    example_my_channel_slugs(j)
    example_my_channel_slugs_and_series_slugs(j)

    the_purpose_of_all_this_v1()
    the_purpose_of_all_this_v2()

    print_channel_slugs()
    print_channel_slugs(titles_too=True)
    print_series_slugs()
    print_series_slugs(titles_too=True)

    """
    channels = None
    word, series = 'Sta', 'star-trek-discovery-de,star-trek-enterprise-de'
    word, series = 'Sta', None
    word, series = None, 'star-trek-discovery-de'
    word, series, channels = None, None, 'pluto-tv-star-trek-de'
    print_after_all_filters(find_in_series_name=word,
                            my_channel_slugs=channels,
                            my_series_slugs=series,
                            print_count=True)


if __name__ == "__main__":
    # print(pluto_url_around_now())
    testing_all_of_the_above()
    # the_purpose_of_all_this_v2()
    # print_channel_slugs(titles_too=True)
    # print_channel_slugs()
    # print_series_slugs()
    # print_series_slugs(titles_too=True)
