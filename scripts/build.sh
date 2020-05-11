#!/usr/bin/env bash

set -ex

export PYTHONDONTWRITEBYTECODE=1

rm -rf /home/logic/_workspace/kicad_workspace/kicad/kicad_library/kicad-footprints/footprint-lib.pretty/130_130_heatbed-route.kicad_mod

python3 heatbed.py

# done