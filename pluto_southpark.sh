#!/bin/bash

loc=de # es,fr,de,uk, ...

series="south-park-"$loc
channels="comedy-central-south-park-"$loc

source .venv/bin/activate

command='python -m plutoalert Search -t \"South Park\"'

echo $command
$command
