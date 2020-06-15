import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/coffee')
import cafe

@patch('builtins.input', side_effect=["3"])
def test_buy_cafe(mock_input):
    if 'cafe' in sys.modules:
        del sys.modules["cafe"]
        import cafe
    tab = {
        "water": 200,
        "milk": 440,
        "coffee beans": 108,
        "disposable cups": 8,
        "money": 556
    }
    assert cafe.buy() == tab

@patch('builtins.input', side_effect=["2000", "500", "100", "10"])
def test_fill_cafe(mock_input):
    if 'cafe' in sys.modules:
        del sys.modules["cafe"]
        import machine_a_cafe
    tab = {
        "water": 2400,
        "milk": 1040,
        "coffee beans": 220,
        "disposable cups": 19,
        "money": 550
    }
    assert cafe.fill() == tab

@patch('builtins.input', side_effect=[""])
def test_fill_cafe(mock_input):
    if 'cafe' in sys.modules:
        del sys.modules["cafe"]
        import cafe
    tab = {
        "water": 400,
        "milk": 540,
        "coffee beans": 120,
        "disposable cups": 9,
        "money": 0
    }
    assert cafe.take() == tab

    """
Write action (buy, fill, take, remaining, exit):
> remaining
 
The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money
 
Write action (buy, fill, take, remaining, exit):
> buy
 
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!
 
Write action (buy, fill, take, remaining, exit):
> remaining
 
The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money
 
Write action (buy, fill, take, remaining, exit):
> buy
 
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!
 
Write action (buy, fill, take, remaining, exit):
> fill
 
Write how many ml of water do you want to add:
> 1000
Write how many ml of milk do you want to add:
> 0
Write how many grams of coffee beans do you want to add:
> 0
Write how many disposable cups of coffee do you want to add:
> 0
 
Write action (buy, fill, take, remaining, exit):
> remaining
 
The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money
 
Write action (buy, fill, take, remaining, exit):
> buy
 
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!
 
Write action (buy, fill, take, remaining, exit):
> remaining
 
The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money
 
Write action (buy, fill, take, remaining, exit):
> take
 
I gave you $564
 
Write action (buy, fill, take, remaining, exit):
> remaining
 
The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money
 
Write action (buy, fill, take, remaining, exit):
> exit
"""

