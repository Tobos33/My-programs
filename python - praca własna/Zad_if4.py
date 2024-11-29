#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:03:33 2024

@author: user
"""
x = int(input("podaj liczbę nr 1 "))
y = int(input("podaj liczbę nr 2 "))
z = int(input("podaj liczbę nr 3 "))

if x >= y and x >= z and y >= z: print(z,y,x)
elif x <= y and x >= z and y >= z: print(z,x,y)
elif x >= y and x >= z and y <= z: print(y,z,x)
elif x >= y and x <= z and y <= z: print(y,x,z)
elif x <= y and x <= z and y >= z: print(x,z,y)
elif x <= y and x <= z and y <= z: print(x,y,z)

