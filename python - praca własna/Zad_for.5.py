#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:41:46 2024

@author: user
"""

lista = [9, 41, 12, 3, 74, 15]
x = 0

for i in lista:
    if lista.index(i) == 0:
        print(i, "jest najmniejsze")
        x = i
    else:
        if i < x:
            print(i, "<", x)
            x = i
            print(x, "jest najmniejsze")  
        elif i > x:
            print(x, "<", i)
            print(x, "jest najmniejsze")  
    