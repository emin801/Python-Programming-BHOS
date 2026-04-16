#Tasks

from random import *

def leng(List):
    s=0
    for i in List:
        s+=1
    return s

#Task 1
'''
def yoxlama(List,eded):
    k=0
    t=0
    while k<leng(List):
        if List[k]==eded:
            print(f"List[{k}]={eded}")
            t+=1
        k+=1
    if t==0:
        print("Tapilmadi")
    else:
        print("Tapildi!")
        
List=[randint(0,5) for i in range(5)]
print(f"Massiv:{List}")
eded=int(input("Ne axtaririq:"))
yoxlama(List,eded)'''

#Task 2
'''
def reqem_cemi(eded):
    s=0
    while eded>0:
        s+=eded%10
        eded//=10
    return s

def bubble_sorting(List):
    n=leng(List)
    for i in range(n-1):
        for j in range(n-2,i-1,-1):
            if reqem_cemi(List[j])>reqem_cemi(List[j+1]):
                List[j],List[j+1]=List[j+1],List[j]
    return List

List=[randint(100,1000) for i in range(10)]
print(f"List:{List}")
print(bubble_sorting(List))'''


#Task 3
'''
def bubble_sorting(List):
    n=leng(List)
    for i in range(n-1):
        for j in range(n-2,i-1,-1):
            if List[j]>List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    return List

print("5 setri daxil edin:")
List=[]

for i in range(1,6):
    soz=input(f"{i}.")
    List+=[soz]

print(bubble_sorting(List))'''

#Task 5
'''
from random import randint
def uzun(List):
    s = 0
    for i in List:
        s += 1
    return s

def bubble_sorting(List):
    N = uzun(List)
    for i in range(N-1):
        for j in range(N-2, i-1, -1):
            if List[j+1] < List[j]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

def reverse_sorting(List):
    N = uzun(List)
    for i in range(N-1):
        for j in range(N-2, i-1, -1):
            if List[j+1] > List[j]:
                List[j], List[j+1] = List[j+1], List[j]
    return List


List=[randint(-100,100) for x in range(10)]
print(f"List: {List}")
List=reverse_sorting(List)

L1=List[:5]
L2=List[5:]

L1=bubble_sorting(L1)
L2=reverse_sorting(L2)
RESULT=L1+L2
print(f"Netice:{RESULT}")'''

#Task 6
'''
def uzun(List):
    s = 0
    for i in List:
        s += 1
    return s

def bubble_sorting(List):
    N = uzun(List)
    for i in range(N-1):
        for j in range(N-2, i-1, -1):
            if List[j+1] < List[j]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

def functionizm(List):
    plusList=[]
    minusList=[]
    say=0
    for i in List:
        if i>0:
            plusList+=[i]
            say+=1
        else:
            minusList+=[i]
    print(f"Musbet elementlerin sayi:{say}")
    plusList=bubble_sorting(plusList)
    minusList=bubble_sorting(minusList)[::-1]
    print(f"{plusList+minusList}")
            

from random import randint
N=int(input("Listin uzunluqu:"))
List=[randint(-100,100) for x in range(N)]
print(f"List: {List}")

functionizm(List)'''

#Task 7
'''
def bubble_sort(List):
    sayan=0
    N=leng(List)
    for i in range(N-1):
        for j in range(N-2,i-1,-1):
            if List[j+1]<=List[j]:
                List[j],List[j+1]=List[j+1],List[j]
                sayan+=1
    return sayan

def selection_sorting(List):
    N=leng(List)
    sayan=0
    for i in range(N-1):
        emin=i
        for j in range(i+1,N):
            if List[j]<List[emin]:
                emin=j
        if i!=emin:
            List[emin],List[i]=List[i],List[emin]
            sayan+=1
    return sayan


List1=[randint(1,1000) for i in range(1000)]
List2=[randint(1,1000) for i in range(1000)]
List3=[randint(1,1000) for i in range(1000)]
List4=[randint(1,1000) for i in range(1000)]
List5=[randint(1,1000) for i in range(1000)]
List6=[randint(1,1000) for i in range(1000)]
List7=[randint(1,1000) for i in range(1000)]
List8=[randint(1,1000) for i in range(1000)]
List9=[randint(1,1000) for i in range(1000)]
List10=[randint(1,1000) for i in range(1000)]

cem1=bubble_sort(List1)+bubble_sort(List2)+bubble_sort(List3)+bubble_sort(List4)+bubble_sort(List5)
cem2=selection_sorting(List6)+selection_sorting(List7)+selection_sorting(List8)+selection_sorting(List9)+selection_sorting(List10)

print(f"average changes for bubble sorting:{cem1/5}")
print(f"average changes for selection sorting:{cem2/5}")'''


#Task 8
'''
def leng(A):
    s=0
    for i in A:
        s+=1
    return s

def bubble_sort(A):
   N = leng(A)
   for i in range(N - 1):
       for j in range(N - i - 1):
           if A[j] > A[j + 1]:
               A[j], A[j + 1] = A[j + 1], A[j]
   return A

def binary_search(A, target):
   left = 0
   right = leng(A) - 1
   count = 0
   while left <= right:
       mid = (left + right) // 2
       count += 1
       if target == A[mid]:
           return mid, count
       else:
           if target > A[mid]:
               left = mid + 1
           else:
               right = mid - 1
   return -1

arr = [1, 4, 7, 3, 9, 2, 4, 5, 2]
print("Massiv:", end = "")
for i in arr: print(i, end = " ")
bubble_sort(arr)
print("\nCheshidlenmeden sonra:", end = "")
for i in arr: print(i, end = " ")

X = int(input("\nX ededi daxil edin: "))

count = binary_search(arr, X)[1]
index = binary_search(arr, X)[0]

if index == -1:
   print("Tapilmadi")
else:
   print(f"Tapildi. A[{index}] = {X}")
   print(f"Muqayise sayi: {count}")
'''
#Task 10
'''
def bubble_sorting(List):
    n=leng(List)
    for i in range(n-1):
        for j in range(n-2,i-1,-1):
            if List[j]>List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    return List

def binary_search(List,x):
    left=0
    right=leng(List)-1
    while left<=right:
        mid=(left+right)//2
        if x==List[mid]:
            return f"{mid}-ci indeksde Tapildi! {List[mid]}"
        else:
            if x>List[mid]:
                left=mid+1
            else:
                right=mid-1
    if List[mid]!=x:
        a=1
        while x not in List:
            y=x-a
            z=x+a
            a+=1
            if y in List:
                return f"Tapilmadi,En yaxin eded:{y}"
            if z in List:
                return f"Tapilmadi,En yaxin eded:{z}"
                
            
List=[randint(0,10) for i in range(10)]
print(f"Massiv:{List}")
List=bubble_sorting(List)
print(f"Cesidlemeden sonra:{List}")
x=int(input("Eded:"))
print(f"{binary_search(List,x)}")'''

#Task 11
'''
def tek(l1):
    tlist=[]
    for i in l1:
        k=0
        while i>0:
            if (i%10)%2==1:
                k+=1
            i//=10
        tlist+=[k]
    return tlist
        
def cut(l2):
    clist=[]
    for i in l2:
        k=0
        while i>0:
            if (i%10)%2==0:
                k+=1
            i//=10
        clist+=[k]
    return clist

def bubble_sorting1(l1, tlist):
    n = leng(l1)
    for i in range(n - 1):
        for j in range(n -i-1):
            if tlist[j] > tlist[j + 1]:
                tlist[j], tlist[j + 1] = tlist[j + 1], tlist[j]
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
    return l1

def bubble_sorting2(l2, clist):
    n = leng(l2)
    for i in range(n - 1):
        for j in range(n - i -1):
            if clist[j] < clist[j + 1]:
                clist[j], clist[j + 1] = clist[j + 1], clist[j]
                l2[j], l2[j + 1] = l2[j + 1], l2[j]
    return l2

    
List=[randint(100,999) for i in range(6)]
print(f"Massiv:{List}")
l1=List[:leng(List)//2]
l2=List[leng(List)//2:]
clist=cut(l2)
tlist=tek(l1)
print(f"Ilk yarisi: {l1}")
print(f"son yarisi: {l2}")
print(f"Tek reqemlerin sayi ilk yarida:{tek(l1)}")
print(f"Cut reqemlerin sayi son yarida: {cut(l2)}")
print(bubble_sorting1(l1,tlist)+bubble_sorting2(l2,clist))'''

#Task 12
'''
def no_zeros(List):
    nozerocountlist=[]
    for i in List:
        k=0
        while i>0:
            if i!=0:
                k+=1
            i//=10
        nozerocountlist+=[k]
    return nozerocountlist

def reqem_cemi(List):
    reqemcemleri=[]
    for i in List:
        k=0
        while i>0:
            k+=i%10
            i//=10
        reqemcemleri+=[k]
    return reqemcemleri

def selection_sorting1(list1,list3):
    N=leng(list1)
    for i in range(N-1):
        emin=i
        for j in range(i+1,N):
            if list3[j]<list3[emin]:
                emin=j
        if i!=emin:
            list1[emin],list1[i]=list1[i],list1[emin]
            list3[emin],list3[i]=list3[i],list3[emin]
    return list1

def selection_sorting2(list2,list4):
    N=leng(list2)
    for i in range(N-1):
        emin=i
        for j in range(i+1,N):
            if list4[j]<list4[emin]:
                emin=j
        if i!=emin:
            list2[emin],list2[i]=list2[i],list2[emin]
            list4[emin],list4[i]=list4[i],list4[emin]
    return list2

N=int(input("intervalin son ededi:"))
mylist=[randint(1,N) for i in range(8)]
list1=mylist[:leng(mylist)//2]
list2=mylist[leng(mylist)//2:]
list3=no_zeros(list1)
list4=reqem_cemi(list2)
print(f"mylist={selection_sorting1(list1,list3)+selection_sorting2(list2,list4)}")'''




















    
