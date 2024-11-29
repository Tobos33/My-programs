#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:42:24 2024

@author: user
"""

nazwa = ["Prąd", "Opór", "Napięcie", "Moc"]
I = "3E-3 10E-3 30E-3"
R = "3.5 4.2 6.8"
I2 = list(map(float, I.split()))
R2 = list(map(float, R.split()))
U = []
P = []
for i,j in zip(I2, R2):
    U.append(i*j)
    P.append((i**2)*j)
print(nazwa)
for k, l, m, n in zip(I2, R2, U, P):
    print(k, l, m, n)
print(" ".join(nazwa))