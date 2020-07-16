# test_credit.py
import pytest
from unittest import mock
from unittest.mock import patch
import argparse
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/credit')
from credit import mess_error, init, diff_payment, annuity_payments, annuity_principal, credit


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type=None,
                principal=1000000,
                periods=60,
                interest=10,
                payment=None
                )
            )
def test_error_type(args):
    args = args()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mess_error(args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="diff",
                principal=1000000,
                periods=None,
                interest=10,
                payment=100000
                )
            )
def test_error_type(args):
    args = args()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mess_error(args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="annuity",
                principal=1000000,
                periods=8,
                interest=None,
                payment=10400
                )
            )
def test_error_type(args):
    args = args()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mess_error(args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="annuity",
                principal=1000000,
                periods=None,
                interest=None,
                payment=10400
                )
            )
def test_error_type(args):
    sys.argv=[
        "toto",
        'type='+ args.type,
        'principal='+ args.principal,
        'payment='+ args.payment
    ]
    args = args()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mess_error(args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 10

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="diff",
                principal=30000,
                periods=-14,
                interest=10,
                payment=None
                )
            )
def test_error_type(args):
    sys.argv=[
        "toto",
        'type='+ args.type,
        'principal='+ args.principal,
        'periods='+ args.periods,
        'interest='+ args.interest
    ]
    args = args()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mess_error(args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 20

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="diff",
                principal=1000000,
                periods=10,
                interest=10,
                payment=None
                )
            )
def test_diff_payment(args):
    tab = [
        108334,
        107500,
        106667,
        105834,
        105000,
        104167,
        103334,
        102500,
        101667,
        100834
    ]
    args = args()
    interest = (args.interest / 100) / (12 * 1)
    payd_out = 0
    for i in range(1, args.periods + 1):
        payd_out = diff_payment(
            args.principal,
            args.periods,
            interest,
            i
        )
        assert tab[i - 1] == payd_out

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="annuity",
                principal=1000000,
                periods=60,
                interest=10,
                payment=None
                )
            )
def test_diff_payment(args):
    args = args()
    interest = (args.interest / 100) / (12 * 1)
    assert annuity_payments(args.principal, args.periods, interest) == 21248

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="annuity",
                principal=None,
                periods=120,
                interest=5.6,
                payment=8722
                )
            )
def test_diff_principal(args):
    args = args()
    interest = (args.interest / 100) / (12 * 1)
    assert annuity_principal(args.payment, args.periods, interest) == 800018

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(
                type="annuity",
                principal=500000,
                periods=None,
                interest=7.8,
                payment=23000
                )
            )
def test_credit(args):
    args = args()
    interest = (args.interest / 100) / (12 * 1)
    assert credit(args.payment, args.principal, interest) == 24
