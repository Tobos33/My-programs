#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:27:39 2024

@author: user
"""

x = input("podaj liczbę z przedziału od 0 do 1 " )
try:
    y = float(x)
    if y > 1 or y < 0: print("liczba spoza przedziału")
    elif y <= 0.6: print("F")
    elif y <= 0.7: print("D")
    elif y <= 0.8: print("C") 
    elif y <= 0.9: print("B") 
    else: print("A")
except:
    print("Nie jest to liczba")
    