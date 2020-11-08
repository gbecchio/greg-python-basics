# test_bankaccount.py
import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/bankaccount')
import bankaccount

def test_luhn_algorithm():
    _tmp_response = bankaccount.luhn_algorithm("4000004938320896")
    assert _tmp_response == True
    _tmp_response = bankaccount.luhn_algorithm("4000003075958775")
    assert _tmp_response == False
    _tmp_response = bankaccount.luhn_algorithm("4000001939016675")
    assert _tmp_response == False

@patch('builtins.input', side_effect=["1234567890123456", "1234"])
def test_logging_false(mock_input):
    assert bankaccount.logging() == False

def test_create_card():
    _tmp_id = bankaccount.create_card()
    assert len(str(_tmp_id)) == 16
    assert len(bankaccount.tab[_tmp_id]) == 4

@patch('builtins.input', side_effect=["4000008449433403", "2560"])
def test_logging_pass(mock_input):
    print(bankaccount.tab)
    bankaccount.tab["4000008449433403"] = "2560"
    print(bankaccount.tab)
    assert bankaccount.logging() == "4000008449433403"

# test
# 1. Create an account
# 2. Log into account
# 0. Exit
# >1
#  
# Your card has been created
# Your card number:
# 4000004938320895
# Your card PIN:
# 6826
#  
# 1. Create an account
# 2. Log into account
# 0. Exit
# >2
#  
# Enter your card number:
# >4000004938320895
# Enter your PIN:
# >4444
#  
# Wrong card number or PIN!
#  
# 1. Create an account
# 2. Log into account
# 0. Exit
# >2
#  
# Enter your card number:
# >4000004938320895
# Enter your PIN:
# >6826
#  
# You have successfully logged in!
#  
# 1. Balance
# 2. Log out
# 0. Exit
# >1
#  
# Balance: 0
#  
# 1. Balance
# 2. Log out
# 0. Exit
# >2
#  
# You have successfully logged out!
#  
# 1. Create an account
# 2. Log into account
# 0. Exit
# >0
#  
# Bye!# 