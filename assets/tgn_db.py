import json
import sqlite3
import requests

tgn_prefix = 'http://vocab.getty.edu/tgn/'
tgn_db_conn = sqlite3.connect('assets/tgn_db.db')
tgn_cursor = tgn_db_conn.cursor()


def tgn_cache(geo_code):
    dbquery = db_query(geo_code)
    if dbquery is not None:
        return dbquery
    else:
        db_write(geo_code)
        return db_query(geo_code)


def db_query(geo_code):
    token = (geo_code,)
    tgn_cursor.execute('SELECT * FROM tgn WHERE code=?', token)
    return tgn_cursor.fetchone()
    

def db_write(geo_code):
    tgn_place = geo_code + '-place.jsonld'
    place = requests.get(tgn_prefix + tgn_place)
    if place.status_code == 200:
        place_json = json.loads(place.text)
        lat = place_json['http://www.w3.org/2003/01/geo/wgs84_pos#lat']['@value']
        long = place_json['http://www.w3.org/2003/01/geo/wgs84_pos#long']['@value']
        tgn_cursor.execute('INSERT INTO tgn VALUES (?, ?, ?, ?)', (geo_code, lat, long, "temp"))
        tgn_db_conn.commit()
