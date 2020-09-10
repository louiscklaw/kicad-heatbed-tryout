#!/usr/bin/env bash

export PYTHONDONTWRITEBYTECODE=1

set -ex

rm -rf /home/logic/_workspace/kicad_workspace/kicad/kicad_library/kicad-footprints/footprint-lib.pretty/130_130_heatbed-route.kicad_mod

python3 heatbed.py

# done
