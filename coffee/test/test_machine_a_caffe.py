import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/coffee')
import machine_a_cafe

@patch('builtins.input', side_effect=["3"])
def test_buy_cafe(mock_input):
    if 'machine_a_cafe' in sys.modules:
        del sys.modules["machine_a_cafe"]
        import machine_a_cafe
    tab = {
        "water": 200,
        "milk": 440,
        "coffee beans": 108,
        "disposable cups": 8,
        "money": 556
    }
    assert machine_a_cafe.buy() == tab

@patch('builtins.input', side_effect=["2000", "500", "100", "10"])
def test_fill_cafe(mock_input):
    if 'machine_a_cafe' in sys.modules:
        del sys.modules["machine_a_cafe"]
        import machine_a_cafe
    tab = {
        "water": 2400,
        "milk": 1040,
        "coffee beans": 220,
        "disposable cups": 19,
        "money": 550
    }
    assert machine_a_cafe.fill() == tab

"""
The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money
 
Write action (buy, fill, take):
> take
I gave you $550
 
The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
0 of money
"""
@patch('builtins.input', side_effect=[""])
def test_fill_cafe(mock_input):
    if 'machine_a_cafe' in sys.modules:
        del sys.modules["machine_a_cafe"]
        import machine_a_cafe
    tab = {
        "water": 400,
        "milk": 540,
        "coffee beans": 120,
        "disposable cups": 9,
        "money": 0
    }
    assert machine_a_cafe.take() == tab