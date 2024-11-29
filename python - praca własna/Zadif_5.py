#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:16:05 2024

@author: user
"""

x = float(input("podaj pensję "))
h = float(input("podaj liczbę godzin "))
if h <= 40: print(x*h)
else: print(x*40+x*(h-40)*1.5)