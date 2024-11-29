#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:10:57 2024

@author: user
"""

liczby = input("Podaj liczby (bez zera): ")
lista = list(map(int, liczby.split()))
ujemne = []
for i in lista:
    if i < 0:
        ujemne.append(i)
print("lista:", ujemne,"\nsuma:", sum(ujemne))