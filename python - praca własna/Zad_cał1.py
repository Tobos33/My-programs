#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:38:16 2024

@author: user
"""

def funkcja(X, Y):
    if X >= 0 and Y >= 0:
        print("pierwsza ćwiartka")
    elif X <= 0 and Y >= 0:
        print("druga ćwiartka")
    elif X <= 0 and Y <= 0:
        print("trzecia ćwiartka")
    elif X >= 0 and Y <= 0:
        print("czwarta ćwiartka")
    else:
        print("leży na osi X albo na osi Y")
x = int(input())
y = int(input())
funkcja(x,y)
        