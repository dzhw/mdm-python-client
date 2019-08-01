#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mdm_python_client.mdm_client import get_study, get_instrument, get_survey, get_question, get_dataset, get_variable, \
    get_publication

__author__ = "René Reitmann"
__copyright__ = "DZHW GmbH"
__license__ = "AGPL-3.0"

test_api_endpoint = "https://metadatamanagement-test.cfapps.io/api"


def test_get_study():
    study = get_study("stu-gra2005$", test_api_endpoint)
    assert "DZHW" in study.title.de
    assert hasattr(study, 'doi')


def test_get_study_not_found():
    study = get_study("hurz", test_api_endpoint)
    assert study is None
    
    
def test_get_survey():
    survey = get_survey("sur-gra2005-sy1$", test_api_endpoint)
    assert survey is not None


def test_get_survey_not_found():
    survey = get_survey("hurz", test_api_endpoint)
    assert survey is None


def test_get_instrument():
    instrument = get_instrument("ins-gra2005-ins1$", test_api_endpoint)
    assert instrument is not None


def test_get_instrument_not_found():
    instrument = get_instrument("hurz", test_api_endpoint)
    assert instrument is None
    
    
def test_get_question():
    question = get_question("que-gra2005-ins1-1.1$", test_api_endpoint)
    assert question is not None


def test_get_question_not_found():
    question = get_question("hurz", test_api_endpoint)
    assert question is None
    
    
def test_get_dataset():
    dataset = get_dataset("dat-gra2005-ds1$", test_api_endpoint)
    assert dataset is not None


def test_get_dataset_not_found():
    dataset = get_dataset("hurz", test_api_endpoint)
    assert dataset is None


def test_get_variable():
    variable = get_variable("var-gra2005-ds1-astu011a$", test_api_endpoint)
    assert variable is not None


def test_get_variable_not_found():
    variable = get_variable("hurz", test_api_endpoint)
    assert variable is None
    
    
def test_get_publication():
    publication = get_publication("pub-Kratz.2016$", test_api_endpoint)
    assert publication is not None


def test_get_publication_not_found():
    publication = get_publication("hurz", test_api_endpoint)
    assert publication is None