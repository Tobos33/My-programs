#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:44:58 2024

@author: user
"""

import numpy as np
plik = open("szafir SiO2 20 mkm.dat", "r")

U3x = []
#U1 = []
F = []
#Ts2 = []
#Tsp = []
#Tck = []
Ts1 = []
#Rs = []
#Po = []
Io = 25*(10**-3)
lista = []

j = -1
for i in plik:
    try:
        lane = list(map(float, i.split()))
        if lane[0] > 1:
            #Tsp.append(lane [0])
            #Tck.append(lane [1])
            Ts1.append(lane[2])
            #Rs.append(lane[3])
            #Po.append(lane[4])
            j += 1
            U3x.append(lista.copy())
            #U1.append(lista.copy())
            F.append(lista.copy())
            #Ts2.append(lista.copy())
        else:
            U3x[j].append(lane[0])
            #U1[j].append(lane[3])
            F[j].append(lane[4])
            #Ts2[j].append(lane[5])
                
    except:
        continue
    
T = np.array(Ts1)
U3w = np.array(U3x)
fr = F[0]   
b = 10**-5
R = 0.0425*T+10.8
cw0 = -12.46816+ 0.02185*T+0.00324*(T**2)-1.10811*(10**-5)*(T**3) + 1.15185*(10**-8)*(T**4)
g = 4000
l = 1840*(10**-6)
d = 335*(10**-9)
cw = cw0/0.10196
#print(cw)
U1 = R*Io
#print(U1)
P = U1**2/R
z = 0
for k in F[0]:
    if k != 100:
        z += 1
    else:
        break
y = 0
for j_3 in F[0]:
    if j_3 != 1000:
        y += 1
    else:
        break        
U3w_mi = []
U3w_ma = []
for n in range(len(Ts1)):
    U3w_mi.append(U3w[n][z])
    U3w_ma.append(U3w[n][y])
U3w_min = np.array(U3w_mi)
U3w_max = np.array(U3w_ma)


lamb_sub_1 = (U1**3)*np.log(10)*0.0425/(4*np.pi*l*(R**2)*(U3w_min-U3w_max))
#print(lamb_sub_1) 

alfa = lamb_sub_1/(g*cw)
f_sr = sum(fr[z:y+1])/len(fr[z:y+1])
#print(f_sr)

U3w_sr = []
for o in range(len(U3x)):
    U3w_sr.append(sum(U3w[o][z:y+1])/len(U3w[o][z:y+1]))
#print(U3w_sr)
#print(U1)

omega = 2*np.pi*f_sr
dT_s = P*(0.5*np.log(alfa/(b**2))-0.5*np.log(2*omega)+1)/(np.pi*l*lamb_sub_1)
#print(dT_s)

U3w_sr_tab = np.array(U3w_sr)
dT = 2*U3w_sr_tab*R/(0.0425*U1)
#print(dT)
dT_f = dT - dT_s
lamb_F_1 = P*d/(2*b*l*dT_f)
#print(lamb_F_1)
q_1 = 10**-4
q_2 = 5*(10**-5)

f_100 = alfa/(4*np.pi*(q_1**2))
f_50 = alfa/(4*np.pi*(q_2**2))
#print(f_100, f_50)
lista_z = []
lista_y = []
z = 0
for p in f_100:
    for q in fr:
        if q < p:
            z += 1
        else:
            lista_z.append(z)
            z = 0
            break
y = -1
for s in f_50:
    for u in fr:
        if u < s:
            y += 1
        else:
            lista_y.append(y)
            y = -1
            break  
        
f_1 = []
f_2 = []
U3w_1 = []
U3w_2 = []
#print(lista_z)

j_1 = 0
for v in lista_z:
    f_1.append(fr[v])
    U3w_1.append(U3x[j_1][v])
    j_1 += 1
#print(U3w_1)

j_1 = 0
for x in lista_y:
    f_2.append(fr[x])
    U3w_2.append(U3x[j_1][x])
    j_1 += 1
    

f_1_tab = np.array(f_1)
f_2_tab = np.array(f_2)
U3w_1_tab = np. array(U3w_1)
U3w_2_tab = np.array(U3w_2)
print(f_1_tab, f_2_tab)
print(U3w_1_tab, U3w_2_tab)

lamb_sub_2 = (U1**3)*np.log(f_2_tab/f_1_tab)*0.0425/(4*np.pi*l*(R**2)*(U3w_1_tab-U3w_2_tab))

#print(lamb_sub_2)
alfa_2 = lamb_sub_2/(g*cw)
#print(alfa_2)

f_sr_2 = []
for i_1, j_2 in zip(f_1, f_2):
    f_sr_2.append(sum(fr[fr.index(i_1):fr.index(j_2)+1])/len(fr[fr.index(i_1):fr.index(j_2)+1]))
#print(f_sr_2)
U3w_sr_222 = []
x_1 = 0
#print(U3x)
'''for k_1 in range(len(U3w_1)):
    U3w_sr_222.append(sum(U3x[k_1][U3x.index(U3w_1[k_1]):U3x.index(U3w_2[k_1])+1]))/len(U3x[k_1][U3x.index(U3w_1[k_1]):U3x.index(U3w_2[k_1])+1])
   '''
U3w_lista = []
f_lista = []

j = 0
for n_1, m_1, ff_1, ff_2 in zip(F, U3x, f_1, f_2):
    U3w_lista.append([])
    f_lista.append([])
    for s_1, p_1 in zip(n_1, m_1):
        if s_1 >= ff_1 and s_1 <= ff_2:
            f_lista[j].append(s_1)
            U3w_lista[j].append(p_1)
        elif s_1 > ff_2:
            j+=1 
            break
U3w_sr_lista = []
f_sr_lista = []
for v_1, w_1 in zip(U3w_lista, f_lista):
    U3w_sr_lista.append(sum(v_1)/len(v_1))
    f_sr_lista.append(sum(w_1)/len(w_1))
#print(U3w_sr_lista)
#print(f_sr_lista)
#print()
#print(f_sr_2)   


f_sr_tab = np.array(f_sr_lista)
omega_2 = 2*np.pi*f_sr_tab        
    
    
dT_s_2 = P*(0.5*np.log(alfa_2/(b**2))-0.5*np.log(2*omega_2)+1)/(np.pi*l*lamb_sub_2)
#print(dT_s)


U3w_sr_tab_2 = np.array(U3w_sr_lista)
dT_2 = 2*U3w_sr_tab_2*R/(0.0425*U1)
print(dT_2)


dT_f_2 = dT_2-dT_s_2
print(dT_f_2)

lamb_F_2 = P*d/(2*b*l*dT_f_2)
print(lamb_F_2)


import matplotlib.pyplot as plt
plt.scatter(Ts1, lamb_F_1)
plt.scatter(Ts1, lamb_F_2) 
plt.show()
plt.scatter(Ts1, lamb_sub_1)
plt.scatter(Ts1, lamb_sub_2)
plt.show()
plt.scatter(Ts1,dT_s)
plt.scatter(Ts1, dT)
plt.show()
