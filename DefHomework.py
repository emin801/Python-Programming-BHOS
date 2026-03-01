'''Sual 1
try:
    def cem():
        toplam=0
        while True:
            eded=int(input("Eded:"))
            if eded== -1:
                break
            else:
                toplam+=eded
        return toplam
    
    def check():
        if cem()%2==0:
            return True
        else:
            return False
    
    if check():
        print("Cutdur")
    else:
        print("Tekdir")
except:
    print("Error")'''


'''Sual 2
try:
    def sert(a,b):
        if (a//b)%2==0:
            return True
        else:
            return False

    a,b=map(int,input("Ededler:").split())

    print(sert(a,b))
except:
    print("Error")'''


'''Sual 3
try:
    def sert(n,k):
        if k**2==n:
            return True
        else:
            return False

    n,k=map(int,input("Ededler:").split())
    print(sert(n,k))
except:
    print("Error")'''


'''Sual 4
def pronic_heteromic(p,n):
    if p==n*(n+1):
        return True
    else:
        return False

p=int(input("Eded1:"))
n=int(input("Eded2:"))
    
if pronic_heteromic(p,n):
    print("Pronic")
else:
    print("Heteronic")'''
    

'''Sual 5
def uzunluq(eded):
    uzun=0
    eded=abs(eded)
    while eded>0:
        uzun+=1
        eded//=10
    return uzun
eded=int(input("Eded:"))
print(uzunluq(eded))'''


'''Sual 6
def uzunluq(N):
    uzun=0
    N=abs(N)
    while N>0:
        uzun+=1
        N//=10
    return uzun

def disarium(N):
    uzun=uzunluq(N)
    cem=0
    while N>0:
        cem+=(N%10)**uzun
        uzun-=1
        N//=10
    return cem

N=int(input("Eded:"))
if N==disarium(N):
    print("Disariumdur")
else:
    print("Disarium eded deyil")'''


'''Sual 7
def curzon(N):
    if (2**N+1)%(2*N+1) == 0:
        return True
    else:
        return False
    
N=int(input("Eded:"))
if curzon(N):
    print("Curzon ededdir")
else:
    print("Curzon eded deyil")'''


'''Sual 8
from math import factorial
def kempner(eded):
    num=1
    while True:
        if factorial(num)%eded==0:
            break
        else:
            num+=1
    return num

eded=int(input("Eded:"))
print(kempner(eded))'''


'''Sual 9
def reqem_cemi(eded):
    cem=0
    while eded>0:
        cem+=eded%10
        eded//=10
    return cem

def qismet(eded):
    cem=reqem_cemi(eded)
    return eded//cem

def Moran():
    portion=qismet(eded)
    for num in range(2,portion):
        if portion%num==0:
            return False
    else:
        return True

eded=int(input("Eded:"))
if Moran():
    print("Moran")
else:
    print("Non-Moran")
print(Moran())'''


'''Sual 10
def sert1(x):
    ilk_reqem=x%10
    while x>10:
        x//=10
    son_reqem=x
    kv_kok=(ilk_reqem+son_reqem)**0.5
    return kv_kok

def sert2():
    if sert1(x)>3:
        return True
    else:
        return False
    
x=int(input("Eded:"))

if sert2():
    print("boyukdur")
else:
    print("boyuk deyil")'''


'''Sual 11
def ebob(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a

    #a=b= ebob(a,b)
    return a

def function():
    if ebob(a,b)==1:
        return True
    else:
        return False

a=int(input("Eded1:"))
b=int(input("Eded2:"))


if function():
    print("qarsiliqli Sadedirler")
else:
    print("Deyiller")'''


'''Sual 12
def uzun(eded):
    length=0
    while eded>0:
        length+=1
        eded//=10
    return length

def sade(a):
    for i in range(2,a):
        if a%i==0:
            return False
    else:
        return True

def hiper_sade(eded):
    say=0
    while eded>0:
        if sade(eded):
            say+=1
        eded//=10
    return say

def ilk_reqem(eded):
    while eded>9:
        eded//=10
    if eded==1:
        return False
    else:
        return True

eded=int(input("Eded:"))

if hiper_sade(eded)==uzun(eded):
    if ilk_reqem(eded):
        print(f"{eded} ededi hiper-sadedir.")
    else:
        print(f"{eded} ededi hiper-sade deyil.")
else:
    print(f"{eded} ededi hiper-sade deyil.")'''


'''Sual 13
def ebob(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    # a=b=ebob(a,b)
    return a

def ekob(a,b):
    ekob=a*b/ebob(a,b)
    return int(ekob)

a=int(input("Eded1:"))
b=int(input("Eded2:"))

print(f"Ebob{a,b}={ebob(a,b)}")
print(f"Ekob{a,b}={ekob(a,b)}")'''


'''Sual 14
def muqayise(a,b,c):
    if a!=b!=c:
        if a>=b>=c:
            print(c,b,a,end=" ")
        if b>=a>=c:
            print(c,a,b,end=" ")
        if a>=c>=b:
            print(b,c,a,end=" ")
        if b>=c>=a:
            print(a,c,b,end=" ")
        if c>=a>=b:
            print(b,a,c,end=" ")
        if c>=b>=a:
            print(a,b,c,end=" ")
    else:
        print("Artan sira ile duzmek olmur")

a=int(input("Eded1:"))
b=int(input("Eded2:"))
c=int(input("Eded3:"))

muqayise(a,b,c)'''


'''Sual 15
def ebob(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def sadelesdirme(a,b):
    sade_a=a//ebob(a,b)
    sade_b=b//ebob(a,b)
    return f"Sadelesdirmeden sonra:{sade_a}/{sade_b}"

a,b=map(int,input("a ve b ni daxil edin:").split())
print(sadelesdirme(a,b))'''


'''Sual 16
def uzunluq(x):
    length=-1
    while x>0:
        length+=1
        x//=10
    return length

def ters(x):
    lengt=uzunluq(x)
    ters_eded=0
    while x>0:
        ters_eded+=(x%10)*10**lengt
        lengt-=1
        x//=10
    return ters_eded

x=int(input("Eded:"))
print(f"Ters eded:{ters(x)}")'''