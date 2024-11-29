#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:03:27 2024

@author: user
"""

aa = [1000, 5000, 500, 250]
bb = [15, 88, 543, 964]
cc = [111, 222, 333, 444]
dd = [0.1, 0.006, 4.87, 10.876]
wyniki = []
x = 0
for i, j, k, l in zip(aa, bb, cc, dd):
    x = (i + j/k)/l
    wyniki.append(x)
print(wyniki)