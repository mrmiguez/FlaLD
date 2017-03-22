#!/usr/bin/env python3

import sys
import glob
import json
from os.path import abspath, dirname, join
from FlaLD import FlaLD_DC, FlaLD_MODS, FlaLD_QDC

PATH = join(abspath(dirname(__file__)))

def write_json_ld(docs):
    with open(PATH + 'all-sample2.json', 'a') as jsonOutput:
        json.dump(docs, jsonOutput, indent=2)        

for file in glob.glob(PATH + 'debug/test_data/*Small.xml'):
    if 'fiu' in file:
        write_json_ld(FlaLD_DC(file))
    elif 'fsu' in file:
        write_json_ld(FlaLD_MODS(file))
    elif 'umiami' in file:
        write_json_ld(FlaLD_QDC(file))