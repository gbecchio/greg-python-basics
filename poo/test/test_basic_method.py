# test_basic_method.py

import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/poo')
from basic_method import BasicMethod



def test_basic_method():
    basic_method = BasicMethod("New York")
    assert basic_method.do_smt() == "New York"
    assert BasicMethod.do_smt(basic_method) == "New York"