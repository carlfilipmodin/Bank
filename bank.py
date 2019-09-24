# variablar
user = 0
acc = 0
Password = "0"
balance= 1000
menyloop = True 

LogUser = 0
LogPass = 0
import random


if int(input("[1] Create new account [2] Login")) == 1:
    user = input("Enter your password:")
    password = input("Password: ")
    acc = random.randint(1000,9999)
    pin = int(input("pinCode: "))
else:
    LogUser = input("Username: ")
    LogPass = input("Password: ")
    if LogPass != Password: 
        exit()

print (user, acc, Password, balance, LogPass) 

while menyloop == True: 
    print (" vad vill du göra/veta? ")
    meny = int(input("1 = saldo 2 = insättning 3 = uttag: " ))
    if meny == 1:  
        print ("visa totalt saldo: ", balance )
    elif meny == 2: 
        print ("insättning: ")
        insättning = int(input(""))
        balance += insättning 
        print (" du har satt in =", insättning, "  " "du har nu såhär mycket pengar på kontot ", balance)
    elif meny == 3:
        print ("uttag")
        uttag = int(input(""))
        balance = balance - uttag
        print("du har tagit ut = ", uttag, " du har nu så här mycket pengar kvar ", balance)
        
        