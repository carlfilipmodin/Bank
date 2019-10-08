# variablar
user = 0
# användaren får ett tilldelat värde. 
acc = 0
# Variablen används för att välja om du vill skapa en ny användare eller inte samt tilldelas variablen ett värde.
Password = "0"
# Lösenords och dess värde
balance= 1000
# här kan du välja vilken grund summa pengar på detta konto
menyloop = True 
# Används för att fortsätta att köra loopen på rad 30 tills dess att den stöter på problemet att det inte stämmer eller att något av inputsen inte är definerade, om det är så så slutar programet att köras. 
LogUser = 0
# definerar en input, för ett variabel. samt loggar in på användaren samt sätter ett nytt lösenord på användaren. LogPass jämnför alltså om lösenordet stämmer mot grund lösenordet som i detta fallet är 0 
LogPass = 0
# -------||---------
import random
# Importerar random för att få fram ett slumpat lösenord mellan värdet 1000,9999. Detta för att slippa att kommma på egna lösenord hela tiden. 


if int(input("[1] Create new account [2] Login")) == 1:
    user = input("Enter your password:")
    password = input("Password: ")
    acc = random.randint(1000,9999)
    pin = int(input("pinCode: "))
# if sats som används för att skapa användare och lösenord. med hjälp av Random.randint 
else:
    LogUser = input("Username: ")
    LogPass = input("Password: ")
    if LogPass != Password: 
        exit()
# Else kollar så om något är annars. Och så att det stämmer med grund lösenorden samt användaren. 
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
    else: 
        menyloop = False
# while loop här har har vi alla olika menyer som man kan använda och köra om meny 3 inte stämmer med rätt variabel input så skall detta göras
f= open("Hallo.txt","w+")
f.write(str(balance))
f.close()

if f.mode == "w+":
    contens =f.read()
# denna del används för att öppna en txt fil. om filen som du vill öppna inte existerar så skapas den. 



   