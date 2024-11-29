#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:51:33 2024

@author: user
"""

x = int(input("podaj liczbę nr 1 "))
y = int(input("podaj liczbę nr 2 "))
z = int(input("podaj liczbę nr 3 "))
if x >= y and x >= z: print(x, "jest największe")
elif y >= x and y >= z: print(y, "jest największe")
elif z >= x and z >= y: print(z, "jest największe")