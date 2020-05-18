#!/bin/sh -l

set -e
cp -r /usr/bin/*json /github/workspace/
cp -r /usr/bin/src/ /github/workspace/
export PYTHONPATH=/github/workspace/
export PYTHONUNBUFFERED=1
cd /github/workspace/

python src/main.py "$1" "$2"
