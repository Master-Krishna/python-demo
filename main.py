import random



class Bank:
    def __update(self):
        Database = "data.json"
        Data = [
            {
                "NAME" : self.name,
                "AGE" : self.age,
                "ACCOUNTNO" : self.accountno,
                "PIN" : self.PIN
            }
        ]
            
        try:
            with open(Database,"a") as fs:
                fs.write(Data)
        except Exception as err:
            print(f"An error occurred as {err}")




    def createaccount(self):
        self.name = input("Enter your full name here:- ")
        self.age = int(input("Enter your age here:- "))
        self.accountno = random.randint(4000,5000)
        self.PIN = int(input("Enter your PIN here (4 digit PIN):- "))
        if len(str(self.PIN)) != 4:
            print("Please try again...")
            self.PIN = int(input("Enter your PIN here (4 digit PIN):- "))
        else:
            print("PIN length is correct")

        if self.age < 18:
            return "You are not able to create account because you are below 18...."
        else:
            print("You are able to create your account...verified")

            print(f"Here is your account number please note that - ACCOUNTNO : {self.accountno}")




        






print("if you want to create an account press 1:- ")
print("if you want to check your details press 2:- ")
print("if you want to deposit money press 3:- ")
print("if you want to delete your account press 4:- ")

option = int(input("Enter your repones here:- "))

user = Bank()

if option == 1:
    user.createaccount()