#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from mdm_python_client.skeleton import fib

__author__ = "René Reitmann"
__copyright__ = "René Reitmann"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
