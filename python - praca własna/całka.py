# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:30:37 2024

@author: a.filatova
"""

def hello():
    print('Hello!')
    
hello()

print()

def hello(name):
    print('Hello, ' + name + '!')

hello('people')

print()

# wartosc zwrotna

def hello(name):
    return len(name)

a = hello('people')
print(a)

print()

def funkcja(liczba):
    if liczba < 0:
        return 'Liczba jest ujemna'
    elif liczba > 0:
        return 'Liczba jest dodatnia'
    elif liczba == 0:
        return 'Liczba jest zerem'

liczba = 5
print(funkcja(liczba))

print()

def funkcja(a, b):
    v = a + b
    return v

aa = 6
bb = 4
vv = funkcja(aa, bb)
print(vv)

print()

def funkcja(a, b):
    v1 = a + b
    v2 = a - b
    return v1, v2

aa = 6
bb = 4
vv1, vv2 = funkcja(aa, bb)
print(vv1, vv2)
print(funkcja(aa, bb)[0], funkcja(aa, bb)[1])

print()

def funkcja(b):
    global a
    a = 7
    v = a + b
    return v

a = 6
print('zmienna a przed wywołaniem funkcji:', a)
b = 4
vv = funkcja(b)
print(vv)
print('zmienna a po wywołaniu funkcji:', a)

print()

import scipy.integrate as integrate
import numpy as np

# funkcja podcałkowa
def f(x):
    return x

x_low = 0 # dolna granica całkowania
x_high = 1 # górna granica całkowania

całka = integrate.quad(f, x_low, x_high)[0]
print(całka)

c, error = integrate.quad(f, x_low, x_high)
print(c, error)


val, abserr = integrate.quad(lambda x: np.exp(-x ** 2), -np.inf, np.inf)
print("wynik =", val, "błąd =",abserr)

def func(x, a, b, c):
    n = a + b + c + x
    u = n ** n
    return u

x_1 = 0
x_2 = 5

a, b, c = 2.5, 3.81, 4.9534

v, e = integrate.quad(func, x_1, x_2, args = (a, b, c))
print(v, e)