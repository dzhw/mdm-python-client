# coding=utf-8
from collections import namedtuple

import requests
import requests_cache
import json

requests_cache.install_cache('mdm_api_cache', expire_after=60*60*24)

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())


def _json2obj(data): return json.loads(data, object_hook=_json_object_hook)


def _get_object(url):
    response = requests.get(url)
    # For successful API call, response code will be 200 (OK)
    if response.ok:
        # Loads (Load String) takes a Json file and converts into python data structure (dict)
        return _json2obj(response.content)
    elif response.status_code == 404:
        return None
    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()


# Dies ist die dev system url, stu-gra2005$ ist die ID der Studie, gesamte API Dokumentation ist unter
# https://metadatamanagement-test.cfapps.io/swagger-ui.html zu finden
# baseUrl = 'https://metadatamanagement-test.cfapps.io/api'
# Dies ist die prod system url, stu-gra2005$ ist die ID der Studie
baseUrl = 'https://metadata.fdz.dzhw.eu/api'


def get_study(study_id, endpoint=baseUrl):
    url = endpoint + '/studies/' + study_id
    return _get_object(url)


def get_instrument(instrument_id, endpoint=baseUrl):
    url = endpoint + '/instruments/' + instrument_id
    return _get_object(url)
