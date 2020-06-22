#test_caffe.py
import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/poo')
from caffe import Caffe

def test_action_go():
    caffe = Caffe()
    caffe.action_go("fill")