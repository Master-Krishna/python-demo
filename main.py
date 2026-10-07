class ATM:

    with open("data.json","a") as fs:
        pass



    def CHECKBALANCE(self):
        pass










user = ATM()

print("Check your balance press 1:- ")
print("Deposit Money press 2:- ")
print("Withdraw Money press 3:- ")
print("Change your PIN press 4:- ")
print("Exit press 5:- ")

respones = int(input("Enter your respones here:- "))

if respones == 1:
    user.CHECKBALANCE()