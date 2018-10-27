#Hecho por Inti Velásquez y Miguel Ardon
#Requiere pip para instalar los modulos y Python 3 para correr el programa: 'python main.py'

#to install ---> pip install pyenchant
import enchant
#to install ---> pip install termcolor
from termcolor import colored

import sys, traceback

#english diccionary
checkWord = enchant.Dict("en_US")

#given string
encrypted = ""

#decrypted string
decrypted = ""

def menu():
    print("********Menu*******\n"
           "Opciones:\n"
           "1. PHHW PH DIWHU WKH WRJD SDUWB\n"
           "2. GCUA VQ DTGCM\n"
           "3. Exit\n")
    try:
        return int(input())
    except:
        return 12

def decryptor(word):
    combinations = list()
    decrypted = word
    for alphabet in range(1,27):
        for index in range(0,len(word)):
            asciiValue = ord( word[index] ) + alphabet 
            if asciiValue > 90:
                asciiValue = (ord( word[index] ) - 66) + (alphabet +40)
            #print(word[index], alphabet,  chr(asciiValue) )
            decrypted = list(decrypted)
            decrypted[index] = chr(asciiValue)
            decrypted = "".join(decrypted)
        if checkWord.check(decrypted):
            combinations.append(colored(decrypted,'red') + "")
            #combinations.append(decrypted + "")
            #break
        else:
            #print(decrypted, index, "indice", chr(asciiValue), "valor de letra")
            combinations.append(decrypted + "")            
    return combinations

opcion = 0
while opcion < 3:
    opcion = menu()
    if opcion == 1:
        encrypted = "PHHW PH DIWHU WKH WRJD SDUWB"
    elif opcion == 2:
        encrypted = "GCUA VQ DTGCM"
    else:
        sys.exit(0)    
    
    #pass string to an array
    encryptedList = encrypted.split(" ")
    
    print("Frase encriptada:")
    print(encrypted)
    print("")
    all = list()
    for word in encryptedList:
        all.append(decryptor(word)) 

    for item in range(0,26):
        decryptedWords = int(0)
        decryptedIndex = int(-1)
        for wordColumn in range(0, len(all)):
            try:
                if checkWord.check(all[wordColumn][item]+"") or (not all[wordColumn][item][0].isalnum() and all[wordColumn][item][5].isalnum()):
                    decryptedWords += 1
            except Exception as error:
                loop=1
        print("")
        if decryptedWords == len(encryptedList):
            print("Frase desencriptada:")

        print(item, end='')
        print(".- ", end='')
        palabra = ""        
        for decryptedColumn in range(0, len(all)):
            palabra += all[decryptedColumn][item] + " "
        print(palabra)     
    print("")                                    