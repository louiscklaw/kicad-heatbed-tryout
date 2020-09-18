#!/usr/bin/env python3

import os,sys
from pprint import pprint

TEST_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(TEST_DIR+'/..')

SRC_DIR=PROJ_HOME+'/src'
SRC_LIB=SRC_DIR+'/lib'
SRC_HEATBED=SRC_DIR+'/heatbed'
SRC_K_TEMPLATE=SRC_DIR+'/k_template'

sys.path.append(SRC_DIR)
sys.path.append(SRC_LIB)
sys.path.append(SRC_K_TEMPLATE)
sys.path.append(SRC_HEATBED)

import common
import test_common

import config
import test_config

import kicad_template
import test_kicad_template

import heatbed
import test_heatbed

import test_helloworld

def test_kicad_template_helloworld():
  test_kicad_template.test()

def test_config_helloworld():
  test_config.test()

def test_common_helloworld():
  test_common.test()

def test_heatbed_helloworld():
  test_heatbed.test()

def test():
  test_helloworld.test_helloworld()
  test_common_helloworld()
  test_config_helloworld()
  test_kicad_template_helloworld()
  test_heatbed_helloworld()

if __name__=="__main__":
  test()
