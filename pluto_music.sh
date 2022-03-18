#!/bin/bash

loc=de # es,fr,de,uk, ...

channels="clubbing-tv-"$loc",mtv-unplugged-"$loc",beat-club-"$loc

source .venv/bin/activate

command='python -m plutoalert Search -c '$channels

echo $command
$command
