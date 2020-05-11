#!/usr/bin/env bash

set -ex

export PYTHONDONTWRITEBYTECODE=1

find . | entr -c -s "python3 test.py"

# done