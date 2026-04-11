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

#Task 8
'''
List1 = [1, 2, 3]
List2 = [2, 4, 6]
a=False
for i in List1:
    for k in List2:
        if i==k:
            a=True
    if a:
        print("Var")
        break
else:
    print("Yoxdur")'''

#Task 10
'''
List1 = [3, 4, 6, 7, 23]
List2=[]
def uzun(List1):
    s=0
    for i in List1:
        s+=1
    return s

a=List1[0]
b=List1[1:uzun(List1)]
List2=b+[a]
print(List2)'''

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

#Task 12
'''
List = [5, 7, 5, 9, 2, 6, 4, 3, 2, 5, 6]
cem=0
for i in List:
    if i%2==1:
        cem+=i
    else:
        break
print(f"Ilk cut reqeme qeder olan cem:{cem}")'''

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

#Task 14
'''
from random import *
N=int(input("Listin Olcusu:"))

def funct(eded):
    ferq=abs(eded%10-(eded//10)%10)
    cem=eded%10+(eded//10)%10
    if ferq%2==1 and cem%2==1:
        return True
    
List1=[]
for i in range(N):
    List1+=[randint(100,999)]

List2=[]

for i in List1:
    if funct(i):
        List2+=[i]
print(List2)'''

#Task 17
'''
List1 = [1, 2, 'aasf', '1', '123', 123,-5]
List2=[]
for i in List1:
    try:
        if i>0:
            List2+=[i]

    except:
        continue
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
    maxs=float(-inf)
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

#Task 28
'''
from random import choice

def indeks(soz):
    letters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    a=soz[0]
    for i in range(26):
        if letters[i]==a:
            k=i
            break
    return k

def cumle(a,b,c,d):
    letters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    soz=choice(a)
    firstletter=letters[indeks(soz)+26]
    soz=soz[1:]
    
    Cumle=firstletter+soz+" "+choice(b)+" "+choice(c)+" "+choice(d)+" "+choice(a)+" "+choice(b)+"."
    return Cumle

article_list = ["the", "a", "one", "some", "any"]
noun_list = ["boy", "girl", "dog", "town" , "car"]
verb_list = ["drove", "jumped", "ran", "walked" , "skipped"]
preposition_list = ["to", "from", "over", "under" , "on"]

say=int(input("Cumle sayi:"))
for i in range(say):
    print(cumle(article_list,noun_list,verb_list,preposition_list,),end=" ")'''

#Task 29
'''
print("0-100 arasinda qiymetlerinizi daxil edin:")

eded1=int(input("Fizika fenninin qiymeti: "))
eded2=int(input("Riyaziyyatin qiymeti: "))
eded3=int(input("Kimya fenninin qiymeti: "))
eded4=int(input("Ingilis dilinin qiymeti: "))
eded5=int(input("Ana dilinin qiymeti: "))

List=[eded1]+[eded2]+[eded3]+[eded4]+[eded5]
print(f"Cavablariniz:{List}")

print("Sizin qiymetleriniz:")
a,b,c,d,e=0,0,0,0,0
for i in List:
    if i>90:
        a+=1
    elif i>80 and i<91:
        b+=1
    elif i>70 and i<81:
        c+=1
    elif i>60 and i<71:
        d+=1
    else:
        e+=1
if a!=0:
    print(f"{a} eded A,")
if b!=0:
    print(f"{b} eded B,")
if c!=0:
    print(f"{c} eded C,")
if d!=0:
    print(f"{d} eded D,")
if e==0:
    print("Kesriniz yoxdur.")
else:
    print(f"{e} eded kesriniz var.")'''
