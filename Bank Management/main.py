import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
       if Path(database).exists():
           with open(database) as fs:
              data = json.loads(fs.read())
       else:
          print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def update() :
        with open("data.json" , "w") as fs:
            fs.write(json.dumps(Bank.data))    


    def Createaccount(self):
        info = {
            "name" : input("Tell your name - "),
            "age"  : int(input("Tell your age - ")),
            "email" : input("tell your email - "),
            "pin" : int(input("tell your pin -")),
            "account" : 1234,
            "balance" : 0
        } 
        
        if info ['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry, you cannot create a account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.update()    



user = Bank()


print("press 1 for creating a new account")
print("press 2 for Depositing the money in the bank")
print("press 3 for withdrawing the money from the bank")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response -:"))

if check == 1:
    user.Createaccount()