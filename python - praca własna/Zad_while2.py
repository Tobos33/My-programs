#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:19:39 2024

@author: user
"""

x = int(input("Podaj liczbę"))
i = 1
y = x
while i < y:
    x = i*x
    i += 1
print(x)