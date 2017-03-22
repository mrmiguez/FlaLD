#!/usr/bin/env python3

import sys
import glob
import json
from os.path import abspath, dirname, join
from FlaLD import FlaLD_DC, FlaLD_MODS, FlaLD_QDC

PATH = join(abspath(dirname(__file__)))
print(PATH)

def write_json_ld(docs):
    with open(PATH + 'all-sample2.json', 'a') as jsonOutput:
        json.dump(docs, jsonOutput, indent=2)        

for file in glob.glob('./debug/test_data/*Small.xml'):
    if 'DCdebug' in file:
        #print(abspath(file)) #test
        write_json_ld(FlaLD_DC(abspath(file)))
    elif 'MODSdebug' in file:
        #print(abspath(file)) #test
        write_json_ld(FlaLD_MODS(abspath(file)))
    elif 'QDCdebug' in file:
        #print(abspath(file)) #test
        write_json_ld(FlaLD_QDC(abspath(file)))