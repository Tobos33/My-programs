#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:43:56 2024

@author: user
"""

nogi = int(input("Podaj liczbę nóg "))
oczy = int(input("Podaj liczbę oczu "))
if oczy >= 100 and nogi == 0: print("przegrzebek")
elif oczy == 8 and nogi == 8: print("pająk")
elif nogi == 4 and oczy == 2: print("kot")
elif nogi == 6 and oczy == 2: print("robak")