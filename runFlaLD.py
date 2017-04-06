#!/usr/bin/env python3

import sys
import glob
import json
import logging
import datetime
from os import remove
from os.path import abspath, dirname, join, exists

# pull in config & custom transformation methods
from master_config import CONFIG_DICT
from FlaLD import FlaLD_DC, FlaLD_MODS, FlaLD_QDC

# init logger
logging.basicConfig(filename='error{0}.log'.format(datetime.date.today()), filemode='w', level=logging.DEBUG)

# get current dir and clean if needed
PATH = abspath(dirname(__file__))
if exists(PATH + '/all-sample{0}.json'.format(datetime.date.today())) is True:
    remove(PATH + '/all-sample{0}.json'.format(datetime.date.today()))

def write_json_ld(docs):
    '''
    Simple writing function.
    Will either create and write to file or append.
    '''
    if exists(PATH + '/all-sample{0}.json'.format(datetime.date.today())) is True:
        with open(PATH + '/all-sample{0}.json'.format(datetime.date.today()), 'r') as jsonInput:
            data_in = json.load(jsonInput)
            for record in docs:
                data_in.append(record)
        with open(PATH + '/all-sample{0}.json'.format(datetime.date.today()), 'w') as jsonOutput:
            json.dump(data_in, jsonOutput, indent=2)
    else:
        with open(PATH + '/all-sample{0}.json'.format(datetime.date.today()), 'w') as jsonOutput:
            json.dump(docs, jsonOutput, indent=2)
            
# main loop
# sys.argv[1] should be the top-level repox export dir
for key in CONFIG_DICT.keys():
    file = glob.glob(sys.argv[1] + '{0}*/{0}*.xml'.format(key))[0]
    if CONFIG_DICT[key] == 'qdc':
        write_json_ld(FlaLD_QDC(abspath(file)))
    elif CONFIG_DICT[key] == 'mods':
        write_json_ld(FlaLD_MODS(abspath(file)))
    elif CONFIG_DICT[key] == 'dc':
        write_json_ld(FlaLD_DC(abspath(file)))
