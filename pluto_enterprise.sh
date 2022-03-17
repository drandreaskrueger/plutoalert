#!/bin/bash

source .venv/bin/activate

# restricts to channels pluto-tv-star-trek-de and pluto-tv-sci-fi-de, and searches for Enterprise in SeriesTitle
command="python -m plutoalert Search -c pluto-tv-star-trek-de,pluto-tv-sci-fi-de -t Enterprise"
echo $command

$command
