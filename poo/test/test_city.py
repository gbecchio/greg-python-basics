# test_city.py

import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/poo')
from city import City



def test_cities():
    ny = City("New York", 1624)
    assert ny.name == "New York"
    assert ny.year == 1624

    stockholm = City("Stockholm", 1187)
    assert stockholm.name == "Stockholm"
    assert stockholm.year == 1187

    ny.all_cities.append("New York")
    assert City.all_cities == ["New York"]

    stockholm.all_cities = ["Stockholm"]
    #stockholm.all_cities.append("Stockholm")
    print(stockholm.all_cities)
    assert City.all_cities == ["New York"]