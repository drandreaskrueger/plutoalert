# plutoalert

[![codecov](https://codecov.io/gh/drandreaskrueger/plutoalert/branch/main/graph/badge.svg?token=plutoalert_token_here)](https://codecov.io/gh/drandreaskrueger/plutoalert)
[![CI](https://github.com/drandreaskrueger/plutoalert/actions/workflows/main.yml/badge.svg)](https://github.com/drandreaskrueger/plutoalert/actions/workflows/main.yml)

Awesome plutoalert created by drandreaskrueger

## Clone and initialize virtualenv

```bash
git clone https://github.com/drandreaskrueger/plutoalert.git drandreaskrueger_plutoalert
cd drandreaskrueger_plutoalert
make virtualenv
source .venv/bin/activate
```

## Usage

for now, only one example script is implemented:

```bash
source .venv/bin/activate
python -m plutoalert StarTrek
```
it prints all elements with '**Star Trek**' in the *name* of the series.

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Example output
```
python -m plutoalert StarTrek
Find everything with 'Star Trek' in Series Name:
s00e00 19:00 Feb 28 'Pluto TV Star Trek' 55 mins 'Pluto TV Star Trek' [no-info-available] pluto-tv-star-trek-de
s01e02 19:55 Feb 28 'Das Urteil' 44 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e03 20:39 Feb 28 'Lakaien und Könige' 54 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e04 21:33 Feb 28 'Sprung' 58 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e05 22:31 Feb 28 'Wähle deinen Schmerz' 52 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e01 23:23 Feb 28 'Leuchtfeuer' 49 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e02 00:12 Mar 01 'Das Urteil' 44 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e03 00:56 Mar 01 'Lakaien und Könige' 54 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e04 01:50 Mar 01 'Sprung' 58 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e05 02:48 Mar 01 'Wähle deinen Schmerz' 52 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e01 03:40 Mar 01 'Leuchtfeuer' 49 mins 'Star Trek: Discovery' [star-trek-discovery-de] pluto-tv-star-trek-de
s01e06 04:29 Mar 01 'Doppeltes Spiel' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e07 05:17 Mar 01 'Das Eis bricht' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e08 06:05 Mar 01 'Die Saat' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e09 06:53 Mar 01 'Familienbande' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
s01e10 07:41 Mar 01 'Kalter Krieg' 48 mins 'Star Trek: Enterprise' [star-trek-enterprise-de] pluto-tv-star-trek-de
Series: ['no-info-available', 'star-trek-discovery-de', 'star-trek-enterprise-de']
Channels: ['pluto-tv-star-trek-de']
```
