#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:51:11 2024

@author: user
"""

lista = [1, 2, -5, 8, -7, 0]
nieujemne = []
for i in lista:
    if i <= 0:
        nieujemne.append(i)
print("liczba liczb nieujemnych:", len(nieujemne))
print(nieujemne)

    