
from random import choice as cho
import sys
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
#urceni skryteho-hadaneho cisla, nejdrive vytvorime list s nahodnymi cisly
for i in range(0,4):
    number = cho(numbers)
    numbers.remove(number)
    li.append(number)

#z listu nahodnych cisel vytvorim skryte-hledane cislo n
nasobek = 1
hledane_cislo =0
for i in li:
    hledane_cislo += i*nasobek
    nasobek *= 10


#funkce urcena k transformaci zadaneho cisla do listu
def t(g):
    x = []
    for i in range(1,5):
        x.append(g%(10))
        g //=10
    return x

#funkce duplic ma zjistit, zda  cisle nejsou duplicitni hodnosty
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
    #
    uzivatel_vstup = input(f"\n Tak do toho, zadej svůj tip! pokus č.{pokus}\n (čtyrmístné číslo nebo e - exit)......  ")
    pr()


    if uzivatel_vstup == "e":
        sys.exit("Program se ukončuje")
    if not uzivatel_vstup.isnumeric():
        print("Tvé zadání není číslo, zkus to znova")

        continue
    uzivatel_vstup = int(uzivatel_vstup)
    if uzivatel_vstup not in range(1000,10000):
        print("Tvé zadání není v požadovaném rozsahu, \n zkus to znova")

        continue

    if duplic(uzivatel_vstup):
        print("Tvé zadání obsahuje duplicitní hodnoty, \n zkus to znova")

        continue

    bu = 0
    co = 0
    #transformuji hledane cislo a uzivatelsky vstup do listu
    c1 = t(hledane_cislo)

    h1 = t(uzivatel_vstup)
    #zjistim pocet bulls - stejna cisla na stejne pozici
    for i in range(0,4):
        if c1[i]==h1[i]:
            bu+=1

    # a nyni se zamerim na cows - rozlozim listy z hledaneho cisla a uzivatelskeho vstupu do dictionary
    count1 = Counter(c1)
    count2 = Counter(h1)
    #prevedu si je na sety
    k1 = set(count1.keys())
    k2 = set(count2.keys())
    #tyto sety pak porovnam
    sk = k1.intersection(k2)

    #nasledne zkoumam prunik techto setu
    for i in sk:
        if count1[i] >= count2[i]:
            co += count2[i]
        else:
            co += count1[i]
    if uzivatel_vstup ==hledane_cislo:
        print(f"Úžasné!!!, uhodl ji číslo na {pokus}. pokus")
        time.sleep(5)
        sys.exit("Zvítězil jsi, hra se ukončuje")
    pr()
    #ted je tady ta chyba - cows jsem v zadani chapal jen jako promennou k ulozeni poctu stejnych cifer v obou cislech
    #kdyz od cows odectu bulls dostanu hodnotu pozadovanou v zadani
    co -=bu
    print(f"bulls:{bu}, cows: {co} \n")
    pr()











