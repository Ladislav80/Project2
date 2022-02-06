from random import randint as ri
from random import choice as cho
import sys
import os
import time
from collections import Counter

def pr():
    print(40*"=")

pr()
print(f"\n Ahoj, vítá tě hra bulls and cows! \n" )
pr()
print(f"\n Mám pro tebe připraveno jedno čtyřmístné \n číslo, zkus ho uhodnout! \n")
pr()
numbers = list(range(1,10))
li = []
for i in range(0,4):
    number = cho(numbers)
    numbers.remove(number)
    li.append(number)
nasobek = 1
n=0
for i in li:
    n += i*nasobek
    nasobek *= 10



def t(g):
    x = []
    for i in range(1,5):
        x.append(g%(10))
        g //=10
    return x

def duplic(x):
    li = []
    d = False
    nasobek = 1
    for i in range(4):
        li.append(x%10)
        x //=10
    for i in range(0,len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                d = True
                break
    return d





pokus = 0
while True:

    pokus += 1
    c = input(f"\n Tak do toho, zadej svůj tip! pokus č.{pokus}\n (čtyrmístné číslo nebo e - exit)......  ")
    pr()

    #os.system("cls")
    if c == "e":
        sys.exit("Program se ukončuje")
    if not c.isnumeric():
        print("Tvé zadání není číslo, zkus to znova")

        continue
    c = int(c)
    if c not in range(1000,10000):
        print("Tvé zadání není v požadovaném rozsahu, \n zkus to znova")

        continue

    if duplic(c):
        print("Tvé zadání obsahuje duplicitní hodnoty, \n zkus to znova")

        continue

    bu = 0
    co = 0
    c1 = t(n)
    #print(c1)
    h1 = t(c)
    #print(h1)
    for i in range(0,4):
        if c1[i]==h1[i]:
            bu+=1
    count1 = Counter(c1)
    count2 = Counter(h1)
    k1 = set(count1.keys())
    k2 = set(count2.keys())
    sk = k1.intersection(k2)

    for i in sk:
        if count1[i] >= count2[i]:
            co += count2[i]
        else:
            co += count1[i]
    if c ==n:
        print(f"Úžasné!!!, uhodl ji číslo na {pokus}. pokus")
        time.sleep(5)
        sys.exit("Zvítězil jsi, hra se ukončuje")
    pr()
    print(f"bulls:{bu}, cows: {co} \n")
    pr()











