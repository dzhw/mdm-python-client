# coding=utf-8
import json
import logging
import os
import tempfile
from collections import namedtuple

import requests_cache


# use a sqllite DB for caching the MDM calls for 24 hours
def __setup_cache():
    # check several directories for write access for the sqllite db
    directories = {tempfile.gettempdir(), "/usr/local/plone_local_files", os.environ.get("TMPDIR", None),
                   os.environ.get("TEMPDIR", None)}
    for cache_dir in directories:
        if cache_dir is not None and os.path.exists(cache_dir) and os.access(cache_dir, os.W_OK):
            print("Going to write cached requests into file:", os.path.join(cache_dir, "mdm_client_cache"
                                                                                       ".sqlite"))
            return requests_cache.CachedSession(cache_name=os.path.join(cache_dir, "mdm_client_cache"),
                                                backend="sqlite", expire_after=60 * 60 * 24, old_data_on_error=True)
    # use memory as fallback
    print("Going to use in-memory cache!")
    return requests_cache.CachedSession(cache_name="mdm_client_cache",
                                        backend="memory", expire_after=60 * 60 * 24, old_data_on_error=True)


_session = __setup_cache()


def __json_object_hook(d): return namedtuple("X", d.keys())(*d.values())


def __json2obj(data): return json.loads(data, object_hook=__json_object_hook)


def __get_object(url):
    """
    Get the json from the given URL and convert it into a python object.

    :param url: The complete url for the GET request.
    :return: A python object created from the response, or None if not found.
    """
    response = _session.get(url)
    # For successful API call, response code will be 200 (OK)
    if response.ok:
        # Loads (Load String) takes a Json file and converts into python data structure (dict)
        return __json2obj(response.content)
    elif response.status_code == 404:
        return None
    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()


# baseUrl = "https://metadatamanagement-test.cfapps.io/api"
baseUrl = "https://metadata.fdz.dzhw.eu/api"


def get_datapackage(datapackage_id, endpoint=baseUrl):
    """
    Get the data package with the given datapackage_id from the MDM. Results will be cached for 24 hours in order to speed up
    subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param datapackage_id: The id of the data package (e.g. "stu-gra2005$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/data-packages/" + datapackage_id
    return __get_object(url)


def get_survey(survey_id, endpoint=baseUrl):
    """
    Get the survey with the given survey_id from the MDM. Results will be cached for 24 hours in order to speed up
    subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param survey_id: The id of the survey (e.g. "sur-gra2005-sur1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/surveys/" + survey_id
    return __get_object(url)


def get_instrument(instrument_id, endpoint=baseUrl):
    """
    Get the instrument with the given instrument_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param instrument_id: The id of the instrument (e.g. "ins-gra2005-ins1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/instruments/" + instrument_id
    return __get_object(url)


def get_question(question_id, endpoint=baseUrl):
    """
    Get the question with the given question_id from the MDM. Results will be cached for 24 hours in order to speed up
    subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param question_id: The id of the question (e.g. "que-gra2005-ins1-1.1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/questions/" + question_id
    return __get_object(url)


def get_dataset(dataset_id, endpoint=baseUrl):
    """
    Get the dataset with the given dataset_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param dataset_id: The id of the dataset (e.g. "dat-gra2005-ds1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/data-sets/" + dataset_id
    return __get_object(url)


def get_variable(variable_id, endpoint=baseUrl):
    """
    Get the variable with the given variable_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param variable_id: The id of the variable (e.g. "var-gra2005-ds1-astu011a$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/variables/" + variable_id
    return __get_object(url)


def get_concept(concept_id, endpoint=baseUrl):
    """
    Get the concept with the given concept_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param concept_id: The id of the concept (e.g. "con-personality$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/concepts/" + concept_id
    return __get_object(url)


def get_publication(publication_id, endpoint=baseUrl):
    """
    Get the publication with the given publication_id from the MDM. Results will be cached for 24 hours in order to
    speed up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/api/swagger-ui.html

    :param publication_id: The id of the publication (e.g. "pub-personality$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/related-publications/" + publication_id
    return __get_object(url)
