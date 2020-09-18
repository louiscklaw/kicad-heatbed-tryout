#!/usr/bin/env python3

import os,sys
from pprint import pprint

TEST_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(TEST_DIR+'/..')
SRC_DIR=PROJ_HOME+'/src'
SRC_LIB=SRC_DIR+'/lib'

sys.path.append(SRC_DIR)
sys.path.append(SRC_LIB)

import common
import test_common

import config

import kicad_template
import test_kicad_template

def test_kicad_template_helloworld():
  kicad_template.helloworld()

def test_config_helloworld():
  config.helloworld()

def test_common_helloworld():
  common.helloworld()
  test_common.test()

def test_helloworld():
  print('helloworld')

def test():
  test_helloworld()
  test_common_helloworld()
  test_config_helloworld()
  test_kicad_template_helloworld()



if __name__=="__main__":
  test()
