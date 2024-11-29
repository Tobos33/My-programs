#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:53:46 2024

@author: user
"""

x = float(input("Podaj wartość x-ów "))
y = float(input("Podaj wartość y-ów "))
if x > 0 and y > 0: print("Pierwsza ćwiartka") 
elif x < 0 and y > 0: print("Druga ćwiartka")
elif x < 0 and y < 0: print("Trzecia ćwiartka")
elif x > 0 and y < 0: print("Czwarta ćwiartka")
elif x == 0 or y == 0: print("Punkt leży na osi x albo y")
