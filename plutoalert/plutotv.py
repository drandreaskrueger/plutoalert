#!/usr/bin/env python
# coding: utf-8

import pprint, json
import requests
import datetime
import urllib.parse

PLUTO_URL_TEMPLATE='http://api.pluto.tv/v2/channels?start={datetime_start}&stop={datetime_end}'
my_channel_slugs=['pluto-tv-sci-fi-de','pluto-tv-star-trek-de', 'doctor-who-classic-de']
my_series_slugs=['star-trek-discovery-de', 'star-trek-discovery-ptv2','star-trek-enterprise-de']


# example_urls:
# example URLs generated in https://github.com/evoactivity/PlutoIPTV
PLUTO_URL_1="http://api.pluto.tv/v2/channels?start=2022-02-20%2023%3A00%3A00.000%2B0100&stop=2022-02-22%2023%3A00%3A00.000%2B0100"
PLUTO_URL="http://api.pluto.tv/v2/channels?start=2022-02-28%2020%3A00%3A00.000%2B0100&stop=2022-03-02%2020%3A00%3A00.000%2B0100"


def create_pluto_url(dt_start, dt_end, template=PLUTO_URL_TEMPLATE):
    params = {"datetime_start": urllib.parse.quote(dt_start+".000+0100"),
              "datetime_end":   urllib.parse.quote(dt_end+".000+0100")}
    url=PLUTO_URL_TEMPLATE.format(**params)
    return url


def create_pluto_url_test(PLUTO_URL):
    # test = create_pluto_url(dt_start="2022-02-20 23:00:00", dt_end="2022-02-22 23:00:00")
    test = create_pluto_url(dt_start="2022-02-28 20:00:00", dt_end="2022-03-02 20:00:00")
    print(PLUTO_URL)
    print(test)
    return test==PLUTO_URL

def pluto_url_around_now(pastdays=0, futuredays=2, time_of_day_string="20:00:00"):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=pastdays)
    yesterday_string = ("%s" % yesterday)[:11] + time_of_day_string
    #print(yesterday_string)
    the_day_after_tomorrow = datetime.datetime.now() + datetime.timedelta(days=futuredays)
    tdat_string = ("%s" % the_day_after_tomorrow)[:11] + time_of_day_string
    #print(tdat_string)
    url = create_pluto_url(yesterday_string, tdat_string)
    return url


def get_pluto_epg(url, ifprint=True):
    # url="http://api.pluto.tv/v2/channels?start=2022-02-27%2023%3A00%3A00.000%2B0100&stop=2022-03-01%2023%3A00%3A00.000%2B0100"
    pluto=requests.get(url)
    j=pluto.json()
    if isinstance(j, dict) and j['statusCode']!=200:
        pprint.pprint(j)
    elif ifprint:
        print("Success. Result list has %d elements." % len(j))
    return j


def extract_channel_slugs_only(j):
    slugs=[]
    for e in j:
        slugs.append(e['slug'])
    slugs=sorted(list(set(slugs)))
    return slugs


def print_with_newlines(j, func=extract_channel_slugs_only):
    res = func(j)
    print("\n".join(res))
    print("#############\n%d elements" % len(res))


def extract_series_slugs_only(j):
    slugs=[]
    for ch in j:
        timelines = ch.get('timelines',[])
        for tl in timelines:
            ep=tl['episode']
            series_slug = ep['series']['slug']
            slugs.append(series_slug)
    slugs=sorted(list(set(slugs)))
    return slugs


def timelines_in_channel(ch, print_channel_name=True, FORMATTER="(%s) %s = %d timelines"):
    timelines = ch.get('timelines',[])
    if print_channel_name:
        print (FORMATTER % (ch['slug'], ch['name'], len(timelines)))
    return timelines


def exxsxx(ep, FORMATTER = "s%02de%02d"):
    season = ep.get('season',0)
    return FORMATTER % (season, ep['number'])


def time_info(tl):
    start = datetime.datetime.strptime(tl['start'][:19],"%Y-%m-%dT%H:%M:%S")
    stop = datetime.datetime.strptime(tl['stop'][:19],"%Y-%m-%dT%H:%M:%S")
    minutes = int((stop-start).total_seconds() / 60.0)
    start_print = start.strftime("%H:%M %b %d")
    return start, start_print, minutes


def series_info(ep):
    series_name = ep['series']['name']
    series_slug = ep['series']['slug']
    return series_name, series_slug


def compile_hit(ep, start_print, minutes,
                series_name, series_slug, ch,
                print_each_hit=False,
                FORMATTER = "%s %s '%s' %s mins '%s' [%s] %s"):
    value=FORMATTER % (exxsxx(ep), start_print, ep['name'], minutes,
                       series_name, series_slug, ch['slug'])
    if print_each_hit:
        print(value)
    return value


def iterate_pluto(j, find_in_series_name=None, 
                  my_channel_slugs=[], my_series_slugs=[], 
                  print_channel_name=True, print_each_hit=False, print_count=True):
    
    hits, ch_slugs, series_slugs = [],[],[]
    for ch in j:
        if not my_channel_slugs or ch['slug'] in my_channel_slugs:
            timelines = timelines_in_channel(ch, print_channel_name)
            for tl in timelines:
                ep=tl['episode']
                series_name, series_slug = series_info(ep)
                
                if find_in_series_name and (find_in_series_name not in series_name):
                    break
                if my_series_slugs and (series_slug not in my_series_slugs):
                    break

                start, start_print, minutes = time_info(tl)
                key=ch['slug']+"_%s"%start # unique key, only 1 thing per time on any channel?
                
                value = compile_hit(ep, start_print, minutes, 
                                    series_name, series_slug, ch,
                                    print_each_hit=print_each_hit)
                    
                hits.append((key,value))
                ch_slugs.append(ch['slug'])
                series_slugs.append(series_slug)
            #break
    if print_count:
        print("\n#################################\n%s elements.\n" % len(hits))
        
    result = sorted(hits, key=lambda x:x[0])
    return result, sorted(list(set(ch_slugs))), sorted(list(set(series_slugs)))


def print_result_series_channels(result, series, channels):
    if not result:
        print ("EMPTY result")
    else:
        print("\n".join(list(zip(*result))[1]))
        print ("Series: %s\nChannels: %s" % (series, channels))


def example_everything(j):
    # careful 2840 answers:
    result, channels, series = iterate_pluto(j, find_in_series_name=False, print_each_hit=False, print_channel_name=False)
    print_result_series_channels(result, series, channels)


def example_Star_in_series_name(j):
    result, channels, series = iterate_pluto(j, find_in_series_name="Star", print_each_hit=False, print_channel_name=False)
    print_result_series_channels(result, series, channels)


def example_Discovery_in_series_name(j):
    result, channels, series = iterate_pluto(j, find_in_series_name="Discovery", print_each_hit=False, print_channel_name=False)
    print_result_series_channels(result, series, channels)


def example_DoctorWho_in_series_name(j):
    result, channels, series = iterate_pluto(j, find_in_series_name="Doctor Who", print_each_hit=False, print_channel_name=False)
    print_result_series_channels(result, series, channels)


def example_my_channel_slugs(j, my_channel_slugs=my_channel_slugs):
    result, channels, series = iterate_pluto(j, 
                                             my_channel_slugs=my_channel_slugs,
                                             print_each_hit=False, print_channel_name=False)
    print_result_series_channels(result, series, channels)


def example_my_channel_slugs_and_series_slugs(j, my_channel_slugs=my_channel_slugs, my_series_slugs=my_series_slugs):
    result, channels, series = iterate_pluto(j, 
                                             my_channel_slugs=my_channel_slugs,
                                             my_series_slugs=my_series_slugs,
                                             print_each_hit=False, print_channel_name=False)
    print_result_series_channels(result, series, channels)


def the_purpose_of_all_this_v1():
    url = pluto_url_around_now(time_of_day_string="20:00:00")
    j = get_pluto_epg(url, ifprint=False)
    result, channels, series = iterate_pluto(j, 
                                             my_channel_slugs=my_channel_slugs,
                                             my_series_slugs=my_series_slugs,
                                             print_each_hit=False, print_channel_name=False, print_count=False)
    print_result_series_channels(result, series, channels)


def the_purpose_of_all_this_v2():
    print("Find everything with 'Star Trek' in Series Name:")
    url = pluto_url_around_now(time_of_day_string="20:00:00")
    j = get_pluto_epg(url, ifprint=False)
    result, channels, series = iterate_pluto(j, find_in_series_name="Star Trek", print_each_hit=False, print_channel_name=False, print_count=False)
    print_result_series_channels(result, series, channels)


# -----------------------------------------------------------------------


def testing_all_of_the_above():
    print(urllib.parse.unquote(PLUTO_URL))
    
    create_pluto_url_test(PLUTO_URL)
    url = pluto_url_around_now()
    print (url)
    PLUTO_URL == url
    
    j = get_pluto_epg(url)
    
    print_with_newlines(j)
    print_with_newlines(j, extract_series_slugs_only)
    
    result, channels, series = iterate_pluto(j, print_channel_name=False, find_in_series_name="Star")
    print_result_series_channels(result, series, channels)
    
    example_everything(j)
    example_Star_in_series_name(j)
    example_Discovery_in_series_name(j)
    example_DoctorWho_in_series_name(j)
    example_my_channel_slugs(j)
    example_my_channel_slugs_and_series_slugs(j)
    
    the_purpose_of_all_this_v1()
    the_purpose_of_all_this_v2()


if __name__ == '__main__':
    testing_all_of_the_above()