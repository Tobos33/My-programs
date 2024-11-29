#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:17:36 2024

@author: user
"""

min = int(input("liczba minut od początku dnia "))
x = min % 60
h = (min - x)/60
print(int(h),":",x,sep="")
