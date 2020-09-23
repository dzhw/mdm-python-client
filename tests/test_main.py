#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdm_python_client.main import main
from mdm_python_client.mdm_client import get_datapackage, get_instrument

__author__ = "René Reitmann"
__copyright__ = "René Reitmann"
__license__ = "AGPL-3.0"

test_api_endpoint = 'https://test.metadata.fdz.dzhw.eu/api'


def test_main_with_data_package_id():
    main(["--datapackage", "stu-gra2005$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_data_package_id():
    main(["--datapackage", "hurz", "--endpoint", test_api_endpoint])


def test_main_with_instrument_id():
    main(["--instrument", "ins-gra2005-ins1$", "--endpoint", test_api_endpoint])


def test_main_with_survey_id():
    main(["--survey", "sur-gra2005-sy1$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_survey_id():
    main(["--survey", "hurz", "--endpoint", test_api_endpoint])


def test_main_with_invalid_instrument_id():
    main(["--instrument", "hurz", "--endpoint", test_api_endpoint])
    
    
def test_main_with_question_id():
    main(["--question", "que-gra2005-ins1-1.1$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_question_id():
    main(["--question", "hurz", "--endpoint", test_api_endpoint])


def test_main_with_dataset_id():
    main(["--dataset", "dat-gra2005-ds1$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_dataset_id():
    main(["--dataset", "hurz", "--endpoint", test_api_endpoint])
    

def test_main_with_variable_id():
    main(["--variable", "var-gra2005-ds1-astu011a$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_variable_id():
    main(["--variable", "hurz", "--endpoint", test_api_endpoint])


def test_main_with_publication_id():
    main(["--publication", "pub-Kratz.2016$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_publication_id():
    main(["--publication", "hurz", "--endpoint", test_api_endpoint])
