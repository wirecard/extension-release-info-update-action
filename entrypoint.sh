#!/bin/sh -l

set -e

python /github/workspace/src/main.py repository "$1" action "$2"
