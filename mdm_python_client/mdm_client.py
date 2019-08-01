# coding=utf-8
import json
import os
import tempfile
from collections import namedtuple

import requests
import requests_cache

# use a sqllite DB for caching the MDM calls for 24 hours
plone_directory = "/usr/local/plone_local_files"
if os.path.exists(plone_directory):
    requests_cache.install_cache(os.path.join(plone_directory, "mdm_client_cache"), expire_after=60 * 60 * 24)
else:
    requests_cache.install_cache(os.path.join(tempfile.gettempdir(), "mdm_client_cache"), expire_after=60 * 60 * 24)


def _json_object_hook(d): return namedtuple("X", d.keys())(*d.values())


def _json2obj(data): return json.loads(data, object_hook=_json_object_hook)


def _get_object(url):
    """
    Get the json from the given URL and convert it into a python object.

    :param url: The complete url for the GET request.
    :return: A python object created from the response, or None if not found.
    """
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


# baseUrl = "https://metadatamanagement-test.cfapps.io/api"
baseUrl = "https://metadata.fdz.dzhw.eu/api"


def get_study(study_id, endpoint=baseUrl):
    """
    Get the study with the given study_id from the MDM. Results will be cached for 24 hours in order to speed up
    subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param study_id: The id of the study (e.g. "stu-gra2005$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/studies/" + study_id
    return _get_object(url)


def get_survey(survey_id, endpoint=baseUrl):
    """
    Get the survey with the given survey_id from the MDM. Results will be cached for 24 hours in order to speed up
    subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param survey_id: The id of the survey (e.g. "sur-gra2005-sur1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/surveys/" + survey_id
    return _get_object(url)


def get_instrument(instrument_id, endpoint=baseUrl):
    """
    Get the instrument with the given instrument_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param instrument_id: The id of the instrument (e.g. "ins-gra2005-ins1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/instruments/" + instrument_id
    return _get_object(url)


def get_question(question_id, endpoint=baseUrl):
    """
    Get the question with the given question_id from the MDM. Results will be cached for 24 hours in order to speed up
    subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param question_id: The id of the question (e.g. "que-gra2005-ins1-1.1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/questions/" + question_id
    return _get_object(url)


def get_dataset(dataset_id, endpoint=baseUrl):
    """
    Get the dataset with the given dataset_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param dataset_id: The id of the dataset (e.g. "dat-gra2005-ds1$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/data-sets/" + dataset_id
    return _get_object(url)


def get_variable(variable_id, endpoint=baseUrl):
    """
    Get the variable with the given variable_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param variable_id: The id of the variable (e.g. "var-gra2005-ds1-astu011a$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/variables/" + variable_id
    return _get_object(url)


def get_concept(concept_id, endpoint=baseUrl):
    """
    Get the concept with the given concept_id from the MDM. Results will be cached for 24 hours in order to speed
    up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param concept_id: The id of the concept (e.g. "con-personality$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/concepts/" + concept_id
    return _get_object(url)


def get_publication(publication_id, endpoint=baseUrl):
    """
    Get the publication with the given publication_id from the MDM. Results will be cached for 24 hours in order to
    speed up subsequent calls. A Rest API explorer can be found here: https://metadata.fdz.dzhw.eu/swagger-ui.html

    :param publication_id: The id of the publication (e.g. "con-personality$")
    :param endpoint: The url of the MDM Api endpoint (default: "https://metadata.fdz.dzhw.eu/api")
    :return: A python object created from the response, or None if not found.
    """
    url = endpoint + "/related-publications/" + publication_id
    return _get_object(url)