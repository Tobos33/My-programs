#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:35:59 2024

@author: user
"""

a = "-5 10 5 0 -5 -10"
lista = list(map(int, a.split()))
x = 10
for i in lista:
    if i > 0:
        if x > i:
            x = i
print(x)