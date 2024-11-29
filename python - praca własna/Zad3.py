#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:08:29 2024

@author: user
"""

n = input("podaj iczbę jabłek ")
k = input("podaj liczbę osób ")
print("każda osoba dostanie", int(int(n)/int(k)),"jabłek.")
print("w koszu zostanie",int(n) % int(k),"jabłek.")