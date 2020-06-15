# test_alien.py

import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/poo')
from alien import Alien



def test_init_places_count():
    mart = Alien("Mars", "martian")
    assert mart.planet == "Mars"
    assert mart.species == "martian"

    dalek = Alien("Scaro", "dalek")
    assert dalek.planet == "Scaro"
    assert dalek.species == "dalek"

    print("aaaaa")
    mart.places.append("Mars")
    mart.count += 1

    dalek.places.append("Scaro")
    dalek.count += 1

    Alien.count += 2


    print(Alien.places)
    assert Alien.places == ['Mars', 'Scaro']
    assert mart.places == dalek.places
    with pytest.raises(AttributeError) as r:
        assert Alien.planet == None
    assert dalek.count == 1
