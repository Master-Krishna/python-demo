import random


class Bank:
    Database = "data.json"
    Data = []

    try:
        with open(Database,"a") as fs:
            rec = fs.write(Data)
    except Exception as err:
        print(f"An error occurred as {err}")




    def createaccount(self):
        name = input("Enter your full name here:- ")
        age = int(input("Enter your age here:- "))
        accountno = random.randint(0,5000,4)
        PIN = int(input("Enter your PIN here:- "))
        


        






print("if you want to create an account press 1:- ")
print("if you want to check your details press 2:- ")
print("if you want to deposit money press 3:- ")
print("if you want to delete your account press 4:- ")

option = int(input("Enter your repones here:- "))

user = Bank()

if option == 1:
    user.createaccount()