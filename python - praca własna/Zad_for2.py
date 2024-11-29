#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:26:45 2024

@author: user
"""

x  = 1
lista = [9, 41, 12, 3, 74, 15]
for i in lista:
    if i > x :
        print(i, "jest większe od ", x)
        x = i
    elif x > i:
        print(x, "jest większe od ", i)