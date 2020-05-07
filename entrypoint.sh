#!/bin/sh -l

set -e

python /usr/bin/main.py repository "$1" action "$2"
