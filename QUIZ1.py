#PYTHON QUIZ 1

#Task 1
'''
def is_perfect_number(eded):
    cem=0

    for nums in range(1,eded):
        if eded%nums==0:
            cem+=nums

    if cem==eded:

        print()
        print(f"Perfect number found: {eded}")
        print("Divisors:",end= " ")

        for nums in range(1,eded):
            if eded%nums==0:
                print(nums,end= " ")
        return True
    else:
        return False
    

while True:
    num1=int(input("Enter start: "))
    num2=int(input("Enter end: "))

    if num2>num1 and num1>0:
        break
    else:
        print("Enter correct!")

say=0
   
for eded in range(num1,num2+1):
    if is_perfect_number(eded):
        say+=1

print()
print(f"Total found: {say}")'''


#Task 2
'''
def sum_digits(eded):
    cem=0
    while eded>0:
        cem+=eded%10
        eded//=10
    return cem

def harshad_chain(eded):
    step=0

    while eded>1:
        if eded%sum_digits(eded)==0:

            step+=1
            print(f"Step {step}: {eded}/{sum_digits(eded)}={eded//sum_digits(eded)}")
            eded//=sum_digits(eded)
            
        else:
            return False
    print(f"Total chain length:{step}")
    return True

eded=int(input("Enter a number (eded>0):"))

if harshad_chain(eded):
    harshad_chain(eded)

else:
    print(0)'''


#Task 3
'''
def max_digit(eded):
    max=1

    while eded>0:
        reqem=eded%10

        if reqem>max:
            max=reqem
        eded//=10

    return max

def count_binary_ones(eded):
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

def is_dominant_trip(eded):
    if max_digit(eded) == count_binary_ones(eded):
        return True
    else:
        return False


eded=int(input("Enter a number (eded>0): "))

print(f"Max digit: {max_digit(eded)}")
print(f"Binary ones count: {count_binary_ones(eded)}")

if is_dominant_trip(eded):
    print(f"Result: {is_dominant_trip(eded)}. It is a Dominant trip number.")
else:
    print(f"Result: {is_dominant_trip(eded)}. It is not a Dominant trip number.")'''


#Task 4
'''
def rotate_number(eded):

    eded1=eded
    say=0

    while eded1>0:
        say+=1
        eded1//=10

    son_num=eded%10
    ilk_num=eded//10**(say-1)
    edo=eded%10**(say-1)-son_num
    new_num=son_num*10**(say-1)+edo+ilk_num

    return new_num

def binary_weight_type(eded):
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

    if say%2==0:
        return 2
    elif say==0:
        return 0
    else:
        return 1
    
def sade(eded):
    for num in range(2,eded):
        if eded%num==0:
            return False
    else:
        return True

def is_perfect_number(eded):
    cem=0

    for nums in range(1,eded):
        if eded%nums==0:
            cem+=nums

    if cem==eded:
        return True
    else:
        return False
    
def analyze_complex_number(eded):
    if sade(eded) and sade(rotate_number(eded)):
        return "Category A"
    
    elif not sade(eded) and binary_weight_type(eded)==2:
        return "Category B"
    
    elif is_perfect_number(eded):
        return "Category C"
    
    else:
        return "Default"

eded=int(input("Enter a number: (eded>0) "))

print(f"Original: {eded}")
print(f"Rotated: {rotate_number(eded)}")
print(f"Binary Weight Type: {binary_weight_type(eded)}")
print(f"Result: {analyze_complex_number(eded)}")'''


#Task 5
'''  
def get_factorial_sum(eded):
    cem=0
    while eded>0:
        num=eded%10

        if num==0 or num==1:
            cem+=1

        else:
            fac=1
            for ededs in range(1,num+1):
                fac*=ededs
            cem+=fac

        eded//=10

    return cem

def is_happy(eded):
    while eded!=1:
        kv_cem=0
        while eded>0:
            kv_cem+=(eded%10)**2
            eded//=10
        eded=kv_cem
        
        if eded==4:
            return False
    return True

eded=int(input("Enter a number:"))
print("------------------------------------")
print(f"Faktoriyal cemi (int):{get_factorial_sum(eded)}")
print(f"Xosbextdirmi? :{is_happy(eded)}")'''
