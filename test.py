'''
File: test.py
Author: Ben Ballard
'''

from digital_roots import additive_digitalroot
from digital_roots import multiplicative_digitalroot
from digital_roots import subtractive_digitalroot

number = input("Number: ")
print("Additive: ")
additive_digitalroot(number)
print("------------------------\nMultiplicative: ")
multiplicative_digitalroot(number)
print("------------------------\nSubtractive: ")
subtractive_digitalroot(number)
