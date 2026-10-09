import random
import json



class Bank:
    
    Database = "data.txt"
    Data = []

    with open(Database,'a') as fs:
        fs.write(Data)


    @staticmethod
    def createaccount():
        pass


        






print("if you want to create an account press 1:- ")
print("if you want to check your details press 2:- ")
print("if you want to deposit money press 3:- ")
print("if you want to delete your account press 4:- ")

option = int(input("Enter your repones here:- "))

user = Bank()

if option == 1:
    user.createaccount()