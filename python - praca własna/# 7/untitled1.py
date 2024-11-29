# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:07:32 2024

@author: a.filatova
"""

import numpy as np

a = [1, 2, 3]
b = [1, 2, 3]
c = [[1, 2, 3], [1, 2, 3]]
d = [[1, 2, 3], [1, 2, 3]]
e = 3

print(a)
print(np.array(a))


print()

print(a + b)   
print(c + d)  

print()

print(np.array(a) + np.array(b))  
print(np.array(c) + np.array(d))   

print()

print(a + c)  
print(np.array(a) + np.array(c))  

print()

print( e * a) 
print(e * np.array(a)) 

print()

print(a + np.array(a))
print(a + np.array(c))

print()

f = []
for i in range(4, 7):
    f.append(i)
ff = np.array(f)
print(ff, type(ff))
g = f + ff
print(g, type(g))

print()
n0 = np.array([[1, 2, 3], [1, 2, 3]])
print('Dodanie rzędu')
n1 = np.append(n0, [[7, 8, 9]], axis=0)
print(n1)
print('Dodanie kolumny')
n2 = np.append(n0, [[7], [8]], axis=1)
print(n2)
print('Brak wskazanej osi')
n3 = np.append(n0, [[7, 8, 9]])
print(n3)

print()
h = np.array([[1, 2, 3], [4, 5, 6]])
print(len(h))
print(h.shape)
print(h[1][2])
print(h[1, 2])

