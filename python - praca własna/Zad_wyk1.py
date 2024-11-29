#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:21:26 2024

@author: user
"""

plika = open("a.txt", "r")
plikb = open("b.txt", "r")

liczbya = list(map(float, plika.split()))
liczbyb = list(map(float, plikb.split()))

plika.close()
plikb.close()

liczby = []

for i, j in zip(liczbya, liczbyb):
    liczby.append(i+j)
    