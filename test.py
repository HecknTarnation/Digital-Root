'''
File: test.py
Author: Ben Ballard
'''

from digital_roots import additive_digital_root
from digital_roots import multiplicative_digitalroot

number = input("Number: ")
print("Additive: ")
additive_digital_root(number)
print("------------------------\nMultiplicative: ")
multiplicative_digitalroot(number)
