#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:35:58 2024

@author: user
"""

lista = [9, 41, 12, 3, 74, 15]
for i in lista:
    print(i)
    print(sum(lista[:lista.index(i)+1]))
    print()