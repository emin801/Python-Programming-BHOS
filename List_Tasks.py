#Task 7
'''
List=[]
for i in range(1,16):
    List+=[i**2]

def ilk_bes(List):
    print("Ilk 5 element = ",end=" ")
    for i in range(5):
        print(List[i],end= " ")

def son_bes(List):
    print("Son 5 element = ",end= " ")
    for i in range(10,15):
        print(List[i],end= " ")

print(f"List= {List}")
ilk_bes(List)
print()
son_bes(List)'''

#Task 11
'''
List1 = ['A', 'B', 'C']
List2 = [1, 2, 3]

def uzun(List1):
    s=0
    for i in List1:
        s+=1
    return s

def cutlesdirme(List1,List2):
    s=uzun(List1)
    List3=[]
    for i in range(s):
        Listo=[List1[i]]+[List2[i]]
        List3+=[Listo]
    return List3
print(cutlesdirme(List1,List2))'''

#Task 13
'''
from random import *
N=int(input("Listin Olcusu:"))

List1=[]

for i in range(N):
    List1+=[randint(10,50)]

List2=[]

for i in List1:
    if i**0.5==int(i**0.5):
        List2+=[i]

print(List1)
print(List2)'''

#Task 18
'''
eded=int(input("Eded daxil edin:"))
List=[]
for i in range(1,eded+1):
    if eded%i==0:
        List+=[i]
print(List)'''

#Task 22
'''
from random import randint
List1=[]
List2=[]

for i in range(10):
    List1+=[randint(0,100)]

def fibanocci(List2):
    List2=[0]
    eded1=0
    eded2=1
    eded3=1
    while eded3<100:
        List2+=[eded3]
        eded3=eded1+eded2
        eded1,eded2=eded2,eded3
    return List2

List=fibanocci(List2)

List3=[]

for i in List1:
    if i in List:
        List3+=[i]
print(List1)
print(List)
print(List3)'''

#Task 23
'''
def smaximum(List):
    maxs=0
    for i in List:
        if maxs<i:
            maxs=i
    
    k=0
    for i in List:
        if i==maxs:
            k+=1
    if k>=2:
        return maxs
    else:
        maxe=0
        for i in List:
            if maxe<i and i<maxs:
                maxe=i
        return maxe

def sminimum(List):
    mins=smaximum(List)
    for i in List:
        if i<mins:
            mins=i
    
    k=0
    for i in List:
        if i==mins:
            k+=1
    if k>=2:
        return mins
    else:
        List= [x for x in List if x!=mins]
        mins=smaximum(List)
        for i in List:
            if i<mins:
                mins=i
        return mins

List=[3,542,5,122,35,52,9,523,444]
print(smaximum(List))
print(sminimum(List))'''

#Task 26
'''
from random import randint
N=int(input("Listin uzunluqu (cut eded):"))
List1=[]
for i in range(N):
    List1+=[randint(100,200)]

print(f"List1:{List1}")

List2=[]
for i in List1:
    cem=0
    while i>0:
        cem+=(i%10)**3
        i//=10
    List2+=[cem]

def ekob(a,b):
    e=a*b
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    eko=e/a
    return eko

List3=[]
for i in range(0,N,2):
    eded1,eded2=List2[i],List2[i+1]
    List3+=[ekob(eded1,eded2)]
print(f"Ekob:{List3}")
'''

#Task 27
'''
def uzun(Massiv):
    s=0
    for i in Massiv:
        s+=1
    return s

def inversiya(Massiv,new):
    u=uzun(Massiv)
    for i in range(u//2):
        num=Massiv[u//2-i-1]
        new+=[num]
    
    for i in range(u//2):
        num=Massiv[u-i-1]
        new+=[num]
    return new
    
    
Massiv=[10,20,30,40,50,60]
new=[]
print(inversiya(Massiv,new))
'''
