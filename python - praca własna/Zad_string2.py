#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:57:14 2024

@author: user
"""

a  = "1; 2; 3; 4; 5; 6"
lista = list(map(int, a.split("; ")))
print(lista, type(lista[0]))