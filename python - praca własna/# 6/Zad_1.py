#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:16:53 2024

@author: user
"""
from sys import exit
plik = open("Si_SiO2 - 22_02_2022.dat", "r")

U3x = []
U1 = []
F = []
Ts2 = []
Tsp = []
Tck = []
Ts1 = []
Rs = []
Po = []
Io = 30*(10**-3)
lista = []
j = -1
for i in plik:
    try:
        lane = list(map(float, i.split()))
        if lane[0] > 1:
            Tsp.append(lane [0])
            Tck.append(lane [1])
            Ts1.append(lane[2])
            Rs.append(lane[3])
            Po.append(lane[4])
            j += 1
            U3x.append(lista.copy())
            U1.append(lista.copy())
            F.append(lista.copy())
            Ts2.append(lista.copy())
        else:
            U3x[j].append(lane[0])
            U1[j].append(lane[3])
            F[j].append(lane[4])
            Ts2[j].append(lane[5])
                
    except:
        continue
#print(Tsp,'\n', Tck,'\n', Ts1,'\n', Rs,'\n', Po,'\n', Io)
#print(U3x, '\n', U1, '\n', F, '\n', Ts2) 

try:
    x = int(input("Podaj temperaturę: "))
    if x > max(Tsp) or x < min(Tsp) : 
        print("Temperatura znajduje się poza zakresem!")
    elif x % 10 != 0:
        print("Temperatura nie jest wielokrotnością 10!")
    else:
        m = 0
        for k in Tsp:
            if k != x:
                m += 1
            elif k == x:
                break
        import matplotlib.pyplot as plt
        plt.scatter(F[m], U3x[m], vmin = 1.5*(10**-4), vmax= 4*(10**-4), label = "U3x")
        plt.yscale("log") 
        plt.xscale("log")
        plt.ylabel("U3x")
        plt.xlabel("f")
        plt.title("Wykres zależności napięcia U3x od częstotliwości dla temp. {} K".format(Tsp[m])) 
        plt.legend()
        plt.show()
        
        
        U1_2 = Rs[m]*Io
        print(U1_2)
        plt.scatter(F[m], U1[m], label = "U1")
        plt.axhline(U1_2, label = "U1 = Rs*Io")
        plt.xscale("log")
        plt.ylabel("U1")
        plt.xlabel("f")
        plt.title("Wykres zależności napięcia U1 od częstotliwości dla temp. {} K".format(Tsp[m])) 
        plt.legend()
        plt.show()
        
        
        plt.scatter(F[m], U3x[m], vmin = 1.5*(10**-4), vmax= 4, label = "U3x")
        plt.scatter(F[m], U1[m], label = "U1")
        plt.yscale("log") 
        plt.xscale("log")
        plt.ylabel("U")
        plt.xlabel("f")
        plt.title("Wykres zależności napięcia U3x od częstotliwości dla temp. {} K".format(Tsp[m])) 
        plt.legend()
        plt.show()
        
        
        plt.scatter(F[m], Ts2[m], c = 'y', label="Temperatura próbki od częstotliwości")
        plt.axhline(Tsp[m], c = 'r', label = "temp wyznaczona przez komputer")
        plt.axhline(Tck[m], c = 'b', label = "temp gornego termometru")
        plt.axhline(Ts1[m], c = 'g', label = "temp próbki")
        plt.xscale("log")
        plt.ylabel("T")
        plt.xlabel("f")
        plt.title("Temperatury dla temp. {} K".format(Tsp[m]))
        plt.legend()
        plt.show()
        
        o = 0
        for n in Tsp:
            plt.scatter(F[o], U1[o], label = "U1 dla {} K".format(Tsp[o]))
            o += 1
        plt.xscale("log")
        plt.ylabel("U1")
        plt.xlabel("f")
        plt.title("Wykres zależności napięcia U1 od częstotliwości dla wszystkich zakresów temperatur") 
        #plt.legend()
        plt.show()
        
        
        o = 0
        for n in Tsp:
            plt.scatter(F[o], U3x[o],  vmin = 1.5*(10**-4), vmax= 4, label = "U3x dla {} K".format(Tsp[o]))
            o += 1
        plt.xscale("log")
        plt.yscale("log")
        plt.ylabel("U1")
        plt.xlabel("f")
        plt.title("Wykres zależności napięcia U1 od częstotliwości dla wszystkich zakresów temperatur") 
        #plt.legend()
        plt.show()
        
        
        
except:
    print("To nie jest liczba")
    
    
    
    
    
    
    
    
    
    
    
    
    
    