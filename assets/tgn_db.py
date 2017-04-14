#! /usr/bin/env python3

import sys
import json
import sqlite3
import requests

tgn_prefix = 'http://vocab.getty.edu/tgn/'


def db_query(geo_code):
    token = (geo_code,)
    tgn_cursor.execute('SELECT * FROM tgn WHERE code=?', token)
    return tgn_cursor.fetchone()
    
def db_write(geo_code):
    print('Writing:')
    tgn_place = geo_code + '-place.jsonld'
    place = requests.get(tgn_prefix + tgn_place)
    if place.status_code == 200:
        place_json = json.loads(place.text)
        lat = place_json['http://www.w3.org/2003/01/geo/wgs84_pos#lat']['@value']
        long = place_json['http://www.w3.org/2003/01/geo/wgs84_pos#long']['@value']
        tgn_cursor.execute('INSERT INTO tgn VALUES (?, ?, ?, ?)', (geo_code, lat, long, "temp"))
        tgn_db_conn.commit()
    
tgn_db_conn = sqlite3.connect('tgn_db.db')
tgn_cursor = tgn_db_conn.cursor()
#tgn_cursor.execute('''CREATE TABLE tgn
#                      (code, lat, long, label)''')
                      
geo_code = sys.argv[1]
dbquery = db_query(geo_code)
if dbquery is not None:
    print('Found!')
    print(dbquery)
else:
    db_write(geo_code)
    print('Resubmitting query...')
    print(db_query(geo_code))
                 