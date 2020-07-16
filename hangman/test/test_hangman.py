# test_hangman.py

import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/hangman')
import hangman



def test_find_all():
    pos = hangman.find_all("java", "a")
    assert list(pos) == [1, 3]
    