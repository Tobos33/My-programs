#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:41:59 2024

@author: user
"""

x = int(input("podaj liczbę trzycyfrową "))
a = int(x/100)
b = int((x - a*100)/10)
c = x - a*100 - b*10
print(a+b+c)