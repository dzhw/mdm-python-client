#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdm_python_client.main import main
from mdm_python_client.mdm_client import get_study, get_instrument

__author__ = "René Reitmann"
__copyright__ = "René Reitmann"
__license__ = "AGPL-3.0"

test_api_endpoint = "https://metadatamanagement-test.cfapps.io/api"


def test_main_with_study_id():
    main(["--study", "stu-gra2005$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_study_id():
    main(["--study", "hurz", "--endpoint", test_api_endpoint])


def test_main_with_instrument_id():
    main(["--instrument", "ins-gra2005-ins1$", "--endpoint", test_api_endpoint])


def test_main_with_invalid_instrument_id():
    main(["--instrument", "hurz", "--endpoint", test_api_endpoint])
