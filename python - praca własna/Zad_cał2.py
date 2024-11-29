#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:45:17 2024

@author: user
"""

def K_na_C(K):
    try:
        if K < 0:
            print("Kelwiny nie mogą być ujemne")
        else:
            C = K - 273
            return C
    except:
        print("Kelwiny muszą być liczbą")
k = 50
print(K_na_C(k))