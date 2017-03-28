#!/usr/bin/env python3

import sys
import glob
import json
from os import remove
from os.path import abspath, dirname, join, exists

# pull in custom tranformation methods
from FlaLD import FlaLD_DC, FlaLD_MODS, FlaLD_QDC


# get current dir and clean if needed
PATH = abspath(dirname(__file__))
if exists(PATH + '/all-sample2.json') is True:
    remove(PATH + '/all-sample2.json')

def write_json_ld(docs):
    '''
    Simple writing function.
    Will either create and write to file or append.
    '''
    if exists(PATH + '/all-sample2.json') is True:
        with open(PATH + '/all-sample2.json', 'a') as jsonOutput:
            json.dump(docs, jsonOutput, indent=2)        
    else:
        with open(PATH + '/all-sample2.json', 'w') as jsonOutput:
            json.dump(docs, jsonOutput, indent=2)
            
# main loop
# sys.argv[1] should be the top-level repox export dir
for file in glob.glob(sys.argv[1] + '*/*Small.xml'):
    '''
    if str tests will need to be changed to match repox export names
    '''
    print(PATH)
    if 'QDC' in file:
        write_json_ld(FlaLD_QDC(abspath(file)))
    elif 'MODS' in file:
        write_json_ld(FlaLD_MODS(abspath(file)))
    elif 'DC' in file:
        write_json_ld(FlaLD_DC(abspath(file)))
     
