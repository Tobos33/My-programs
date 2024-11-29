#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:15:19 2024

@author: user
"""

lista = [10, 5, 0, -5, -10]
x = lista[0]
for i in lista:
    if i > 0:
        if x > i:
            x = i
print(x)