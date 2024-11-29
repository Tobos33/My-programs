#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:30:51 2024

@author: user
"""

import numpy as np

aa = [1000, 5000, 500, 250]
bb = [15, 88, 543, 964]
cc = [111, 222, 333, 444]
dd = [0.1, 0.006, 4.87, 10.876]

wynik = (np.array(aa)+np.array(bb)/np.array(cc))/np.array(dd)
print(wynik)

