#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mdm_python_client.mdm_client import get_study, get_instrument

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


def test_get_instrument():
    instrument = get_instrument("ins-gra2005-ins1$", test_api_endpoint)
    assert instrument is not None


def test_get_instrument_not_found():
    instrument = get_instrument("hurz", test_api_endpoint)
    assert instrument is None
