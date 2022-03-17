#!/bin/bash

source .venv/bin/activate

# Search
# -v verbose = begin with summary of how many hits
# -t titlephrase = None, OR search for titlephrase or -word in SeriesTitle
# -s series = None, OR restrict to given series slugs
# -c channels = None, OR restrict to given channel slugs

# The default
# python -m plutoalert Search -v
# returns EVERYTHING. Careful: ~3000 hits

command="python -m plutoalert Search -v"
echo $command

$command
