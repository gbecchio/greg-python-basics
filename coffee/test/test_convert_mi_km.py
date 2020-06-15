# test_convert_mi_km
import pytest
import sys
sys.path.insert(1, '/home/greg/dev/greg-python-basics/coffee')
import convert_phi

"""
Sample Input : 
100
Sample Output : 
160.9

Sample Input : 
14
Sample Output:
22.526
"""

def test_mi_to_km():
    assert convert_phi.mi_to_km(100) == 160.9
    assert convert_phi.mi_to_km(14) == 22.526

"""
Sample Input : 
451

Sample Output : 
232.778
"""

def test_fahrenheit_to_celsius():
    assert convert_phi.fahrenheit_to_celsius(451) == 232.778
