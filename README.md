# plutoalert

[![CI](https://github.com/drandreaskrueger/plutoalert/actions/workflows/main.yml/badge.svg)](https://github.com/drandreaskrueger/plutoalert/actions/workflows/main.yml)
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/drandreaskrueger/plutoalert)
[![codecov](https://codecov.io/gh/drandreaskrueger/plutoalert/branch/main/graph/badge.svg?token=plutoalert_token_here)](https://codecov.io/gh/drandreaskrueger/plutoalert)

The EPG of Pluto.tv projects only a few hours into the future. This commandline tool here quickly checks, whether the rotation of your favorite series has reached that one episode again, that you have not seen yet.

It begins by downloading the *complete* channel information json (>100 channels, >400 series, >2000 episodes), and then filtering by your choices (see 'ChannelSlug', 'SeriesSlug') - or a simple *word search* within the *title of the series name* (see the 'Star Trek' example).

## Clone and initialize virtualenv
Linux or Mac. For windows see [windows.md](windows.md).

```bash
git clone https://github.com/drandreaskrueger/plutoalert.git drandreaskrueger_plutoalert
cd drandreaskrueger_plutoalert
make virtualenv
source .venv/bin/activate
```

## Usage
For now, 4 example scripts are implemented, they are all called like this:

```bash
source .venv/bin/activate
python -m plutoalert StarTrek
```
it prints all elements with '**Star Trek**' in the *name* of the series.

These *commands* work already (more might be coming):
* `StarTrek`
* `ChannelSlugs`
* `SeriesSlugs`
* `Search` (see the `./pluto_{discovery,enterprise,everything}.sh ` examples below)

Example outputs are below.

## Geoblocking
If the only thing you get is a boring `403 ... EMPTY result` then perhaps the pluto API is *never answering* **to you**? To test it, try `curl http://api.pluto.tv/v2/channels` on the commandline (or paste the URL in a browser). If the answer is `[]` too, then your **solution** is:

First connect your VPN to a country where PlutoTv is working (following list was true in March 2022) ...

* Argentina, Austria, Brazil, Canada, Chile, Costa Rica, France, Germany, Italy, Mexico, Spain, Switzerland, Thailand, UK, US

... and then (first run the curl test above, and then) try `python -m plutoalert StarTrek` again.

### Python online execution environments: pythonanywhere, gitpod, ...
Geoblocking is also the reason why starting plutoalert inside the fabulous [Gitpod](https://gitpod.io/#https://github.com/drandreaskrueger/plutoalert) and [PythonAnywhere](https://www.pythonanywhere.com/gists/94d3b92d57976da77ae2753b45314aeb/plutoalert_StarTrek.py/python3/) ... is executing my Python code just fine ... but is then leading to `EMPTY result`. Sorry for that. Ideas how to solve it?

*Help me: Please* point me to yet another online-Python execution environment, as I would like to present running code to anyone, even those who do not want to install Python locally. Thanks.

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Example output
Star Trek, now with times shown in localzone

```
python3 -m plutoalert StarTrek
command=StarTrek
Find everything with 'Star Trek' in Series Name:
s01e07 05:17 Mar 02 'T=Mudd²' 53 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e20 06:10 Mar 02 'In sicherem Gewahrsam' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e21 06:58 Mar 02 'Vox Sola' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e22 07:46 Mar 02 'Gefallene Heldin' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e23 08:34 Mar 02 'Durch die Wüste' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e24 09:22 Mar 02 'Zwei Tage auf Risa' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e25 10:10 Mar 02 'Die Schockwelle – Teil 1' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e01 10:58 Mar 02 'Die Schockwelle – Teil 2' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e02 11:45 Mar 02 'Carbon Creek' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e03 12:32 Mar 02 'Das Minenfeld' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e04 13:19 Mar 02 'Todesstation' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e05 14:06 Mar 02 'Eine Nacht Krankenstation' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e06 14:53 Mar 02 'Marodeure' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e07 15:40 Mar 02 'Der Siebente' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e08 16:27 Mar 02 'Der Kommunikator' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e09 17:14 Mar 02 'Eigenarten' 47 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s00e00 18:01 Mar 02 'Pluto TV Star Trek' 59 mins 'Pluto TV Star Trek' [no-info-available] pluto-tv-star-trek-de
Series: ['no-info-available', 'star-trek-discovery-de', 'star-trek-enterprise-de']
Channels: ['pluto-tv-star-trek-de']
```

print all channel slugs (-v shows title too)

```
python3 -m plutoalert ChannelSlugs | head -n 15
command=ChannelSlugs
Success. Result list has 133 elements.
action-sports-de
auto-motor-sport-channel-de
avatar-de
bbc-travel-de
beat-club-de
being-human-de
beverly-hills-90210-de
beyblade-burst-de
blaze-de
blues-clues-de
bubble-guppies-de
cc-made-in-germany-de
cc-made-in-germany-de-plus
...
```

print all series slugs (-v shows title too)

```
python3 -m plutoalert SeriesSlugs -v | head -n 15
command=SeriesSlugs
Verbose mode is on.
Success. Result list has 133 elements.
a-harvest-wedding-de = Die Hochzeit des Jahres
a-kid-in-king-arthurs-court = Knightskater - Ritter auf Rollerblades
ab-ins-meer-auf-der-suche-nach-der-verlorenen-perle = Ab ins Meer: Auf der Suche nach der verlorenen Perle
access-all-areas-de = Access All Areas
adventures-of-super-mario-bros-3-de = Adventures of Super Mario Bros 3
aerial-ireland-de = Irland von oben
aerial-new-zealand-de = Neuseeland entdecken
aerial-odyssey-germany-from-above-1-ptv1 = Aerial Odyssey: Germany From Above
africa-from-cape-to-kruger-de = Africa From Cape To Kruger
afrikas-naturparadiese-ptv1 = Afrikas Naturparadiese
alert-threatened-species-de = Vom Aussterben bedroht
alice-durch-den-spiegel = Alice Durch Den Spiegel
...
```

./pluto_discovery.sh

```
python -m plutoalert Search -s star-trek-discovery-de,star-trek-enterprise-de -t Discovery
command=Search
s02e10 02:18 Mar 17 'Der rote Engel' 53 mins 'Star Trek: Discovery DE' [star-trek-discovery-de] pluto-tv-star-trek-de
s02e11 03:11 Mar 17 'Der Zeitsturm' 55 mins 'Star Trek: Discovery DE' [star-trek-discovery-de] pluto-tv-star-trek-de
s02e12 04:06 Mar 17 'Tal der Schatten' 51 mins 'Star Trek: Discovery DE' [star-trek-discovery-de] pluto-tv-star-trek-de
```

 ./pluto_enterprise.sh

```
python -m plutoalert Search -c pluto-tv-star-trek-de,pluto-tv-sci-fi-de -t Enterprise
command=Search
s02e13 04:57 Mar 17 'Morgengrauen' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e14 05:44 Mar 17 'Stigma' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e15 06:31 Mar 17 'Waffenstillstand' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e16 07:18 Mar 17 'Die Zukunft' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e17 08:05 Mar 17 'Canamar' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e18 08:52 Mar 17 'Übergang' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e19 09:39 Mar 17 'Das Urteil' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e20 10:26 Mar 17 'Horizont' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e21 11:13 Mar 17 'Böses Blut' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e22 12:00 Mar 17 'Cogenitor' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e23 12:47 Mar 17 'Regeneration' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e24 13:34 Mar 17 'Erstflug' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
s02e25 14:21 Mar 17 'Kopfgeld' 47 mins 'Star Trek: Enterprise DE' [star-trek-enterprise-de] pluto-tv-star-trek-de
Series: ['star-trek-enterprise-de']
Channels: ['pluto-tv-star-trek-de']
```

./pluto_everything.sh | head -n 12

```
python -m plutoalert Search -v
command=Search
Verbose mode is on.

#################################
2827 elements.

s01e01 02:39 Mar 17 'Dezert People 13 (2016)' 81 mins 'Dezert People 13' [dezert-people-13-ptv2] action-sports-de
s01e01 04:00 Mar 17 'Remote Wakeskates: Good Ratio' 33 mins 'Remote Wakeskates: Good Ratio' [remote-wakeskates-good-ratio-ptv2] action-sports-de
s01e01 04:33 Mar 17 'Good Morning Miyazaki' 38 mins 'Good Morning Miyazaki' [good-morning-miyazaki-ptv2] action-sports-de
s01e01 05:11 Mar 17 'The Golden Era (2014)' 50 mins 'The Golden Era (2014)' [the-golden-era-2014-ptv2] action-sports-de
s01e01 06:01 Mar 17 'All Damn Day' 60 mins 'All Damn Day' [all-damn-day-ptv2] action-sports-de
...
```
