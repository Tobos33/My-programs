#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:05:43 2024

@author: user
"""

x = float(input("Podaj pierwszą liczbę "))
y = float(input("Podaj drugą liczbę "))
z = float(input("Podaj trzecią liczbę "))
if x == y and y == z: print("są trzy liczby o wartości", x)
elif x == y and y != z: print("są dwie liczby o wartości", x)
elif x != y and y == z: print("są dwie liczby o wartości", y)
elif x == z and y != z: print("są dwie liczby o wartości", x)
else: print("Nie ma takich samych liczb")


