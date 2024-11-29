#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:50:20 2024

@author: user
"""

import scipy.integrate as scp
import numpy as np
import matplotlib.pyplot as plt


v = 5703
teta_d = 600
d = 500E-6
A = 1.344E-45
B_u = 1.82E-19
teta = 132
k_b = 1.38E-23
h = 1.054E-34


def C(T, teta_d, v, d, teta, A, B_U):
    k_b = 1.38E-23
    h = 1.054E-34
    calka = scp.quad(lambda x: (((v/d)+(A*(x**4)*(T**4)) 
                                + (((k_b/h)**2)*(x**2)*B_U*(T**3)*np.exp(-teta/T)))**-1)
                     *(x**4)*np.exp(x)/((np.exp(x)-1)**2), 0 ,teta_d/T)
    #print(calka[0])
    return calka[0]

def f(calka, T_1, V):
    k_b = 1.38E-23
    h = 1.054E-34
    lamb = (k_b**4)*(T_1**3)*calka/(2*(np.pi**2)*V*(h**3))
    #print(lamb)
    return lamb

#Całka, error = C(T, teta_d, v, d, teta, A, B_u)
#lamb_GaN = f(C(T, teta_d, v, d, teta, A, B_u)[0], T, v)
#print(lamb_GaN)
T = []
F = []
for i in range (1, 31):
    T.append(i*10)
    c = C(i*10, teta_d, v, d, teta, A, B_u)
    F.append(f(c, i*10, v))
plt.scatter(T, F , c = 'b')
plt.show()

'''v = 6980
teta_d = 950
d = 5.4**-5
A = **-45
B_u = 1.82**-19
teta = 132
k_b = 1.38**-23
h = 1.054**-34'''

