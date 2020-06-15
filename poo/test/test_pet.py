#test_pet.py
import pytest
from unittest import mock
from unittest.mock import patch
import sys

sys.path.insert(1, '/home/greg/dev/greg-python-basics/poo')
from pet import Pet

def test_init():
    pet = Pet("chien", "toto")
    assert pet.spec == "chien"
    assert pet.name == "toto"
    assert pet.legs == 4

def test_class_vars():
    assert Pet.kind == "mammal"
    assert Pet.n_pets == 0
    assert Pet.pet_names == []

    pet1 = Pet("chien", "tata")
    pet2 = Pet("chien", "ratla")
    pet3 = Pet("chien", "d")

    assert pet1.n_pets == 0
    assert pet2.n_pets == 0
    assert pet3.n_pets == 0

    Pet.n_pets = 3
    assert pet1.n_pets == 3
    assert pet2.n_pets == 3
    assert pet3.n_pets == 3