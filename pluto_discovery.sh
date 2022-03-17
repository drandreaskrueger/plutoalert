#!/bin/bash

source .venv/bin/activate

# restricts to SeriesSlugs star-trek-discovery-de,star-trek-enterprise-de, and searches for Discovery in SeriesTitle
command="python -m plutoalert Search -s star-trek-discovery-de,star-trek-enterprise-de -t Discovery"
echo $command

$command
