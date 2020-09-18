#!/usr/bin/env bash

set -ex

python3 ./test/main.py

python3 ./src/main.py output/helloworld-heatbed
