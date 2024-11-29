# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:59:28 2024

@author: a.filatova
"""


# zwykłe otwieranie pliku
file = open('plik do zabawy.txt', encoding = 'utf8')

# odczytanie zawartosci pliku jako ciągu tekstowego
print( '# 1')
content = file.read()
file.close()
print(content)
print(type(content))
print()

print('# 2')
file = open('plik do zabawy.txt')
for line in file:
    print(line)


# nie musimy dodawać encoding, jeżeli w pliku mamy liczby i litery angielskie.
# Ale dla polskiego alfabetu już musimy

print('# 3')
print(file.readlines()) # nic nie ma, bo wszystko już wyssalimy z pliku
print()

# w tym przypadku również będziemy widzieć znaki nowego wiersza
print('# 4')
file = open('plik do zabawy.txt', encoding = 'utf8')
print(file.readlines()) 
file.close()
print()

# Co możemy zrobić z plikiem?
# r - otwarcie do odczytu (domyslne)
file = open('plik do znęcania się.txt', 'r')
print(file.read())
file.close()


# w - otwarcie do zapisu, czysci plik
file1 = open('plik do znęcania się.txt', 'w')
print('Czekam na wakacje', file = file1)
file1.close()
file1 = open('plik do znęcania się.txt', 'r')
print(file1.read())
file1.close()
# x - stworzenie pliku, wyrzuci błąd, jeżeli plik już istnieje

# a - otwarcie do zapisu i dodanie rzeczy do końca pliku
file2 = open('plik do znęcania się.txt', 'a')
print('Bardzo!', file = file2)
file2.close()
file2 = open('plik do znęcania się.txt')
print(file2.read())
file2.close()

file3 = open('plik do znęcania się.txt', 'w')
file3.write('Czekam na wakacje ')
file3.write('Bardzo!')
file3.close()
file3 = open('plik do znęcania się.txt')
print(file3.read())
file3.close()
print()

file4 = open('plik do znęcania się.txt', 'w')
file4.write('Czekam na wakacje \n')
file4.write('Bardzo!\n')
file4.close()
file4 = open('plik do znęcania się.txt')
print(file4.read())
file4.close()

# co jest ważne? Jeżeli otworzylismy plik dla konkretnego celu (na przykład, 'a'), 
# to nie możemy potem z niego niczego przeczytać. Bo będzie błąd!

print()
# Musimy zwracać uwagę na to, co jest w pliku - żeby można było z tym pracować
file = open('plik do zabawy.txt', encoding = 'utf8')
a = []
b = []
c = []
for line in file:
    if len(a) == 0:
        a = list(map(int, line.split()))
    elif len(b) == 0:
        b = list(map(int, line.split()))
    elif len(c) == 0:
        c = list(map(int, line.split()))
    else:
        print(list(line.split()))
for aa, bb, cc in zip(a, b, c):
    print(aa + bb + cc)
        
# matplotlib - do rysunków
import matplotlib.pyplot as plt

a = [1,2,3,4]
b = [5,6,7,8]

c = [5,6,7,8]
d = [9,10,11,12]

k = 300
p = 6

plt.plot(a, b, label = 'linia')
plt.scatter(c, d, label = 'kropki', c = 'r')
plt.yscale('log')
plt.xlabel('a i c')
plt.ylabel('b i d')
plt.axvline(p, c = 'b', label = 'pionowa linia')
plt.axhline(p, c = 'g', label = 'pozioma linia')
plt.title(k)
plt.legend()
plt.show()



    # 'b' as blue

    # 'g' as green

    # 'r' as red

    # 'c' as cyan

    # 'm' as magenta

    # 'y' as yellow

    # 'k' as black

    # 'w' as white

