#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:21:26 2024

@author: user
"""

plika = open("a.txt", "r")
plikb = open("b.txt", "r")

a = plika.read()
b = plikb.read()

liczbya = list(map(float, a.split()))
liczbyb = list(map(float, b.split()))

plika.close()
plikb.close()

liczby = []

for i, j in zip(liczbya, liczbyb):
    liczby.append(i+j)
print (liczby, sum(liczby))