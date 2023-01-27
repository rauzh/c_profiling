#!/bin/bash

./build_apps.sh

if [ -n "$1" ]; then
    ./update_data.sh "$1"
fi

python3 make_preproc.py

./make_postproc.sh
