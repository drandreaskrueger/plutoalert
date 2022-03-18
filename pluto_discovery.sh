#!/bin/bash

loc=de # es,fr,de,uk, ...

series="star-trek-discovery-"$loc",star-trek-enterprise-"$loc",star-trek-discovery-ptv1,star-trek-discovery-ptv2" # ,star-trek-the-next-generation,star-trek-the-next-generation-embed"
channels="pluto-tv-star-trek-"$loc",pluto-tv-sci-fi-"$loc",pluto-tv-sci-fi-series-"$loc",star-trek-1,star-trek-2"

source .venv/bin/activate

# restricts to some SeriesSlugs and then searches for Discovery in SeriesTitle
command="python -m plutoalert Search -s "$series" -t Discovery"

echo $command
$command
