#Task 1
'''
def func(sent):
    new = ""
    prev_space = True
    
    for i in sent:
        if i != " ":
            new += i
            prev_space = False
        else:
            if not prev_space:
                new += " "
                prev_space = True
                
    return new

sent = input("Enter a sentence: ")
print(func(sent))'''

#Task 2
'''
while True:
    
    def uzunluq(bits):
        say=0
        for i in bits:
            say+=1
        return say

    def func(bits):

        for i in bits:
            if i!="0" and i!="1":
                print("Only 0 and 1 s!")
                break
        else:
            if uzunluq(bits)!=8:
                print("That was not 8 bits... Try again!")
            
            else:
                ones=0
                zeros=0
                for i in bits:
                    if i=="1":
                        ones+=1
                if ones%2==0:
                    print("The parity bit should be 0")
                else:
                    print("The parity bit should be 1")
    
    bits=input("Enter 8 bits: ")

    if bits=="end":
        break
    
    func(bits)'''

#Task 3
'''
def pig_latin_translation(word):
    samits="qwrtyplkjhgfdszxcvbnm"
    saits="euioa"
    new_word=""
    if word[0] in samits:
        a=True
        somitos=""
        for i in word:
            if i in samits and a:
                somitos+=i
            else:
                a=False
                new_word+=i
        new_word+=somitos+"ay"

    else:
        new_word+=word+"way"

    return new_word
    

sentence=input("Enter a line of text: ")

print(pig_latin_translation(sentence))'''

#Task 4
'''
def draw_base(width):
    base=width*"="
    return base

def draw_ground_floor(width):
    ground_floor=""
    for i in range(width):
        if i==0 or i==width-1 or i==width//2-1 or i==width//2:
            ground_floor+="|"
        else:
            ground_floor+=" "
    return ground_floor

def draw_floor(width,floors):
    floors=floors-1
    floor=""
    for i in range(width):
        if i==0 or i==width-1:
            floor+="|"
        else:
            floor+=" "
            
    result=""      
    for i in range(floors):
        result+=floor+"\n"
    return result

def draw_roof(width,Roof_type):
    if Roof_type=="flat":
        line=" "+"_"*(width-2)+" "
    else: 
        line = ""
        inside_spaces = 0
        for row in range((width-2)//2):
            spaces = ((width-2)//2 - row )
            line += " " * spaces + "/" + " " * inside_spaces + "\\" + "\n"
            inside_spaces += 2
    return line
    
floors=int(input("Floors (must be at least 2): "))
width=int(input("Width (excluding walls, must be a non-zero even integer): "))
Roof_type=input("Roof type (flat or pointy): ")        

if Roof_type=="pointy":
    house=draw_roof(width,Roof_type)+draw_floor(width,floors)+draw_ground_floor(width)+"\n"+draw_base(width)
else:
    house=draw_roof(width,Roof_type)+"\n"+draw_floor(width,floors)+draw_ground_floor(width)+"\n"+draw_base(width)
print(house)'''


#Task 5
'''
def length(username):
    say=0
    for i in username:
        say+=1
    return say

def is_neighbor_numbers(username):
    leng=length(username)
    numbers="1234567890"
    i=0
    while i<leng-2:
        if username[i] in numbers and username[i+1] in numbers and username[i+2] in numbers and username[i]==username[i+1]==username[i+2]:
            return True
        i+=1
    return False

def is_letter_exist(username):
    letters="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    for i in username:
        if i in letters:
            return False
    else:
        return True
        
def is_number_exist(username):
    numbers="1234567890"
    for i in username:
        if i in numbers:
            return False
    else:
        return True

def is_neighbor_letters(username):
    leng=length(username)
    letters="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    i=0
    while i<leng-2:
        if username[i] in letters and username[i+1] in letters and username[i+2] in letters:
            return True
        i+=1
    return False

def is_space_exist(username):
    for i in username:
        if i==" ":
            return True
    return False

def is_beginning_digit(username):
    if username[0] in "1234567890":
        return True
    return False

username=input("Enter a username: ")

if is_neighbor_numbers(username):
    print("3 same numbers cant be used consequently!")
    
if is_letter_exist(username):
    print("There should be at least 1 letter in username!")
    
if is_number_exist(username):
    print("There should be at least 1 number in username!")
    
if is_neighbor_letters(username):
    print("3 letters should not be used in order!")

if is_space_exist(username):
    print("Space is not allowed in username!")

if is_beginning_digit(username):
    print("Username cannot begin with digit!")'''