import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/coffee')
import c_m

@patch('builtins.input', side_effect=["300", "65", "100", "1"])
def test_eval(mock_input):
    assert c_m.main() == "Yes, I can make that amount of coffee"


