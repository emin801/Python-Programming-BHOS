from random import randint as ra

def create_matrix(a,b):
    M=[]
    for i in range(a):
        M+=[[0]*b]
        for t in range(b):
            M[i][t]=ra(-100,100)
    return M

def print_matrix(M):
    print("Before:")
    for row in M:
        for item in row:
            print(f"{item:4}",end="")
        print()

'''
def sual2(a,b,matrix):

    for t in range(b): 
        sutun = [matrix[r][t] for r in range(a)]
        negatives = [x for x in sutun if x < 0]

        if negatives:  
            print(f"Sütun {t}: mənfi sayı = {len(negatives)}")
        else:       
            print(f"Sütun {t}: cəm = {sum(sutun)}")'''

'''
def sual3(a,b,M):
    for i in range(a):
        for j in range(b):
            if M[i][j]%2==0:
                M[i][j]=M[i][j]//2
            else:
                M[i][j]=M[i][j]**2
    print("After:")           
    for row in M:
        for item in row:
            print(f"{item:4}",end="")
        print()'''

'''
def sual4(a,b,M):
    eb=float('-inf')
    for i in range(a-1):
        for j in range(b-1):
            ikixikicem=M[i][j]+M[i][j+1]+M[i+1][j]+M[i+1][j+1]
            if ikixikicem>eb:
                eb=ikixikicem
    print(eb)'''

'''
def sual5(a,b,M):
    B=create_matrix(a,b)
    for i in range(1,a-1):
        for j in range(1,b-1):
            B[i][j]=M[i][j]+M[i-1][j]+M[i+1][j]+M[i][j-1]+M[i][j+1]
    print()
    for row in B:
        for item in row:
            print(f"{item:4}",end="")
        print()'''

'''
def sual8(M):
    B=[j for i in M for j in i]
    A={}
    L=[]
    for num in B:
        if num in A:
            A[num]+=1
        else:
            A[num]=1
    for i in A:
        if A[i]==1:
            L+=[i]
    s=0
    c=0
    for i in L:
        s+=i
        c+=1
    print(f"cem: {s}, say: {c}")'''

'''
def sual9(a,b,M):
    ebc=float("-inf")
    ekc=float("+inf")
    for i in range(a):
        sutun=[M[j][i] for j in range(b)]
        setir=[M[i][j] for j in range(b)]
        cemsu=0
        cemse=0
        for i in sutun:
            cemsu+=i
        for i in setir:
            cemse+=i
        if cemse>ebc:
            ebc=cemse
        if cemsu<ekc:
            ekc=cemsu
    for i in range(a):
        cemsu=0
        cemse=0
        sutun=[M[j][i] for j in range(b)]
        setir=[M[i][j] for j in range(b)]
        for t in sutun:
            cemsu+=t
        for t in setir:
            cemse+=t
        if cemse==ebc:
            print(setir)
        if cemsu==ekc:
            print(sutun)'''

'''
def sual12(a,b,M):
    for i in range(a):
        for j in range(b):
            if i==0 or j==b//2:
                M[i][j]="+"
            else:
                M[i][j]="0"
    for row in M:
        for item in row:
            print(f"{item:4}",end="")
        print()'''
'''
def sual13(a,b,M):
    for i in range(a):
        for j in range(b):
            if i==j or i+j==b-1:
                M[i][j]="*"
            else:
                M[i][j]="0"

    for row in M:
        for item in row:
            print(f"{item:4}",end="")
        print()'''

'''
def sual16(a,b,M):
    for i in range(a):
        for j in range(b):
            if (i+j)%2==0:
                M[i][j]="1"
            else:
                M[i][j]="0"
    for row in M:
        for item in row:
            print(f"{item:4}",end="")
        print()'''
'''
def sual19(a,b,M):
    t=1
    for i in range(a):
        for j in range(b):
                M[i][j]=t
                t+=1
    for row in M:
        for item in row:
            print(f"{item:4}",end="")
        print()'''

'''
def sual21(a,b,M):
    result=[]
    for j in range(b):
        if j % 2 == 0:
            for i in range(a):
                result += [M[i][j]]
        else:
            for i in range(a - 1, -1, -1):
                result += [M[i][j]]
    for row in result:
        for item in row:
            print(f"{item:4}",end="")
        print()'''


a=int(input("Setir sayi: "))
b=int(input("Sutun sayi: "))

M=create_matrix(a,b)
print_matrix(M)
'''
sual21(a,b,M)'''