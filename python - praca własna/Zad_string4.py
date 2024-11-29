#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:05:48 2024

@author: user
"""

liczby = input("Podaj ciąg liczb rozdzielonych spacjami: ")
lista = list(map(int, liczby.split()))
parzyste = []
for i in lista:
    if i % 2 == 0:
        parzyste.append(i)
print(parzyste)