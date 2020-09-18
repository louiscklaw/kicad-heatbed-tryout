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

def test_config_helloworld():
  config.helloworld()

def test_common_helloworld():
  common.helloworld()

def test_helloworld():
  print('helloworld')

def test():
  test_helloworld()
  test_common_helloworld()
  test_config_helloworld()

  test_common.test()

if __name__=="__main__":
  test()
