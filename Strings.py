 #Task 1
def yoxlama(metn,simvol):
    for i in metn:
        if i==simvol:
            return True
        else:
            return False
metn=input("Metn daxil edin:")
simvol=input("Simvol daxil edin:")
















#Task 7
'''
def uzunluq(qiymet):
    s = 0
    for i in qiymet:
        s += 1
    return s


def evezleme(setr, evezlenen, evezleyici):
    result = ""
    m = uzunluq(setr)
    n = uzunluq(evezlenen)

    i = 0
    while i < m:
        if setr[i:i+n] == evezlenen:
            result += evezleyici
            i += n
        else:
            result += setr[i]
            i += 1

    return result


setr = input("Setri daxil edin: ")
evezlenen = "and"
evezleyici = "&"

print(evezleme(setr, evezlenen, evezleyici))'''

#Task 8
'''
def uzunluq(uzun):
    s=0
    for i in uzun:
        s+=1
    return s

def funksiya(cumle,soz):
    a=uzunluq(cumle)
    b=uzunluq(soz)
    sayan=0
    i=0
    while i<a:
        if cumle[i:i+b]==soz:
            sayan+=1
            i+=b
        else:
            i+=1
    return sayan


cumle=input("Cumle daxil edin:")
soz=input("Axtarilan soz daxil edin:")

print(f"{soz} sozunun sayi: {funksiya(cumle,soz)}")'''

#Task 9
'''
def uzun(soz):
    s=0
    for i in soz:
        s+=1
    return s

def funksiya(string, evezlenen1, evezlenen2, evezedici):
    m=uzun(string)
    n=uzun(evezlenen1)
    k=uzun(evezedici)
    resulto=""
    i=0
    while i<m:
        if (string[i:i+n]==evezlenen1 or string[i:i+n]==evezlenen2) and (i+n==m or string[i+n] in " ,.!?"):
            resulto+=evezedici
            i+=n
        else:
            resulto+=string[i]
            i+=1
    return resulto


string="Bayram günü gələcəyik sizə bayramlasmaqa.Bayramlaşsaz da bayramlaşacağıq. Bayramlaşmasanız da bayramlaşacağıq."
evezlenen1="bayram"
evezlenen2="Bayram"
evezedici="novruz"
print(funksiya(string, evezlenen1, evezlenen2, evezedici))'''

#Task 10
'''
def uzun(soz):
    s=0
    for i in soz:
        s+=1
    return s

def funksiya(string, evezlenen1, evezlenen2, evezedici):
    m=uzun(string)
    n=uzun(evezlenen1)
    k=uzun(evezedici)
    resulto=""
    i=0
    say=0
    while i<m:
        if (string[i:i+n]==evezlenen1 or string[i:i+n]==evezlenen2) and (i+n==m or string[i+n]==" " or string[i+n]==","):
            resulto+=evezedici
            i+=n
            say+=1
        else:
            resulto+=string[i]
            i+=1
    return resulto,f"say:{say}"


string="Haqqı, haqqıya getmiş, Haqqı, haqqıdan haqqını istəmiş, Haqqı, Haqqının haqqını verməyincə, Haqqı da Haqqının haqqından gəlmiş."
evezlenen1="haqqı"
evezlenen2="Haqqı"
evezedici="sari"
print(funksiya(string, evezlenen1, evezlenen2, evezedici))'''

#Task 11
'''
def uzun(soz):
    s = 0
    for i in soz:
        s += 1
    return s


def funksiya(cumle):
    result = ""
    i = 0
    say = 0
    m = uzun(cumle)

    while i < m:
        if cumle[i] == " ":
            result += cumle[i]
            say = 0
        else:
            say += 1
            if say != 2:
                result += cumle[i]
        i += 1

    return result


cumle = input("Cumleni daxil edin: ")
print(funksiya(cumle))'''

#Task 13
'''
def hesablama(cem):
    result = 0
    i = 0
    say = len(cem)

    while i < say:
        while i < say and cem[i] == " ":
            i += 1
        if i >= say:
            break
        eded = ''
        while i < say and cem[i] != "+":
            if cem[i] == " ":
                i += 1
                continue
            eded += cem[i]
            i += 1
        if eded == '':
            return "Yanlis ifade"
        result += int(eded)

        i += 1

    return result


cem = input("Ifadeni daxil edin: ")
print(hesablama(cem))'''

#Task 14
'''
def hesablama(ifade):
    uzun = len(ifade)
    cem = 0
    i = 0
    sign = 1 
    while i < uzun:
        while i < uzun and ifade[i] == " ":
            i += 1
        if i >= uzun:
            break
        num = ""
        while i < uzun and ifade[i] not in "+-":
            if ifade[i] == " ":
                i += 1
                continue
            num += ifade[i]
            i += 1
        if num == "":
            return "Yanlis ifade"
        cem += sign * int(num)

        if i < uzun:
            if ifade[i] == "+":
                sign = 1
            elif ifade[i] == "-":
                sign = -1
            i += 1
    return cem
    
ifade=input("Ifade daxil edin: ")
print(hesablama(ifade))'''

#Task 15
'''
def funksiya(setr):
    uzun=len(setr)
    i=0
    soz=""
    while i<uzun and setr[i] not in ", ":
        soz+=setr[i]
        i+=1
    return soz

setr=input("Setri daxil edin:")
print(f"Birinci soz: {funksiya(setr)}")'''

#Task 16
'''
def genislenme(t):
    i=0
    uzun=len(t)
    while i<uzun and t[i]!=".":
        i+=1
    if i==uzun:
        return "Fayl adinda '.' yoxdur"
    t=t[:i+1]
    t+=Ext
    return t
Tam_ad=input("Faylin tam adini daxil edin:")
Ext=input("Faylin yeni genislenmesini daxil edin:")
print(f"Netice:{genislenme(Tam_ad)}")'''

#Task 17
'''
def yoxlama(ad):
    uzun=len(ad)
    i=0

    if uzun>10:
        return 'Faylin adi 10 simvoldan uzun ola bilmez'
    else:
        while i<uzun:
            if ad[i] in r'/":*<>|':
                return 'Faylin adinda /" : * < > | simvollarindan istifade etmek olmaz.'
                
            i+=1
        return "Faylin adi duzgundur"

            

ad=input("Excel faylinin adi:")
print(yoxlama(ad))'''

#Task 18
'''
def yoxlama(Ad):
    num_counter=0
    symbol_counter=0
    bigletter_counter=0
    smallletter_counter=0
    i=0
    Length=len(Ad)
    while True:

        if Length<5 or Length>15:
            print("Simvol sayi 5 ile 15 arasinda olmalidir")
            break

        else:
            while i<Length:

                if ord(Ad[i])>=48 and ord(Ad[i])<=57:
                    num_counter+=1
                elif ord(Ad[i])>=97 and ord(Ad[i])<=122:
                    smallletter_counter+=1
                elif ord(Ad[i])>=65 and ord(Ad[i])<=90:
                    bigletter_counter+=1
                elif Ad[i] in ".-~_=:":
                    symbol_counter+=1
                else:
                    print("Icazesiz simvollar istifade edilib")
                    break

                i+=1

        if num_counter==0:
            print("Reqem istifade edilmelidir.")
        if smallletter_counter==0:
            print("Kicik herf istifade edilmelidir.")
        if bigletter_counter==0:
            print("Boyuk herf istifade edilmelidir.")
        if symbol_counter==0:
            print("Simvol istifade edilmelidir.")  

        if num_counter>0 and smallletter_counter>0 and bigletter_counter>0 and symbol_counter>0 and i==Length:
            print("Qovluq adi duzgundur")

        break      
Ad=input("Qovluq adi daxil edin: ")
yoxlama(Ad)'''