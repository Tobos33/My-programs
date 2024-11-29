#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:11:29 2024

@author: user
"""

x = float(input("Podaj ile przebiegł sportowiec "))
y = float(input("Podaj limit "))
i = 0
while x <= y:
    x += 0.1*x
    i += 1
else: print(i)
    