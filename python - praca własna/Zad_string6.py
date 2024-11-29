#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:18:29 2024

@author: user
"""

a = "1 2 3 4 5 6 "
b = "1.1 2.2 3.3 4.4 5.5 6.6"
suma = []
for i, j in  zip(list(map(float, a.split())),  list(map(float, b.split()))):
    suma.append(i+j)
print(suma,"\n", sum(suma), sep = '')