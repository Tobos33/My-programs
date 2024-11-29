#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:00:06 2024

@author: user
"""

a = "1; 2; 3; 4; 5; 6;"
lista = list(map(int, a[:-1].split("; ")))
print(lista, type(lista[0]))