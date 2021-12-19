'''
File: digital_roots.py
Author: Ben Ballard
Description: A python module that provides functions from calculating additive digital roots and multiplicative digital roots
'''

if __name__ != "__main__":

    def additive_digital_root(string):
        if len(string) == 1:
            return string
        total = 0
        for i in string:
            total += int(i)
        new_str = str(total)
        print(string + " (" + makeAdditionString(string) + ") -> " + new_str)
        return additive_digital_root(new_str)

    def makeAdditionString(string):
        equation = ""
        for i in string:
            equation += i + " + "
        return equation[0:len(equation)-3]
    
    def multiplicative_digitalroot(string):
        if len(string) == 1:
            return string
        total = int(string[0:1])
        s = string[1:len(string)]
        for i in s:
            total *= int(i)
        new_str = str(total)
        print(string + " (" + makeProductString(string) + ") -> " + new_str)
        return multiplicative_digitalroot(new_str)

    def makeProductString(string):
        equation = ""
        for i in string:
            equation += i + " * "
        return equation[0:len(equation)-3]