#PYTHON QUIZ 2

#Task 1
'''
from math import *
x=float(input("x: "))
y=float(input("y: "))

if ((x**2+y**2)<30 and 2*x-3>y and y>sin(x*pi/180)) or ((x**2+y**2)<30 and y>2*x-3 and y>-3 and y<sin(x*pi/180)):
    print("Daxildir!")
else:
    print("Daxil deyil!")'''


#Task 2
'''
say=int(input("Neçe eded daxil edeceksiniz? "))
k=1
cem=0
found=False
while k<say+1:
    eded=int(input(f"{k}-ci ededi daxil edin: "))

    for nums in range(2,eded):
        if eded%nums==0:
            found=True
            break
    else:
        print(f"{eded} sade ededdir, ceme elave olundu!")
        cem+=eded

    if found:
        print(f"{eded} sade eded deyil! Proses dayanir.")
        break
    
    k+=1

print("-------------------------")
print(f"Yekun cem:{cem}")'''
    

#Task 3
'''
eded=int(input("Tam eded: "))
addim=0
while eded>9:
    eded1=eded
    addim+=1
    cem=0

    while eded>0:
        cem+=eded%10
        eded//=10
    print(f"Addim {addim}: {eded1} reqemleri cemi = {cem}")
    
    eded=cem

print("-------------------------")
print(f"Yekun reqem koku: {eded}")
print(f"Cemi addim sayi: {addim}")'''


#Task 4
'''
def reqem_sayi(eded):
    say=0
    while eded>0:
        say+=1
        eded//=10
    return say

giris=int(input("Start: "))
son=int(input("End: "))

print(f"{giris} ve {son} araligindaki Armstrong ededleri:")
say=0

for num in range(giris,son+1):

    cem=0
    numero=num
    uzun=reqem_sayi(num)

    while num>0:
        cem+=(num%10)**uzun
        num//=10
    
    if cem==numero:
        print(f"Tapildi: {cem} (Reqem sayisi:{uzun})")
        say+=1

print(f"Cemi {say} Armstrong eded tapildi.")'''

    
#Task 5
'''
def sekkizlik(eded):
    eighth=0
    cem=0
    uzun=0

    while eded>0:
        eighth+=(eded%8)*10**uzun
        uzun+=1
        eded//=8

    while eighth>0:
        cem+=eighth%10
        eighth//=10
    
    return cem

def ikilik(eded):
    ikilik=0
    quvvet=0
    say=0

    while eded>0:
        ikilik+=(eded%2)*10**quvvet
        quvvet+=1
        eded//=2
    
    while ikilik>0:

        if ikilik%10==1:
            say+=1
        ikilik//=10

    return say
    
eded=int(input("Musbet tam eded daxil edin:"))

print("---------------------------")
print(f"Daxil edilen eded (Onluq): {eded}")
print(f"Sekkizlik reqemlerinin cemi: {sekkizlik(eded)}")
print(f"Ikilik 1-lerin sayi: {ikilik(eded)}")

if ikilik(eded)==sekkizlik(eded):
    print(f"Netice: True (Eded BALANSLIDIR)")
else:
    print(f"Netice: False (Eded BALANSSIZDIR)")'''


