
import json 
import random
import string
from pathlib import Path


class Bank:
    database = 'D:\python\Bank Managment\data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists.")
    except Exception as err:
        print(f"an exception occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgen(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spc = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spc
        random.shuffle(id)  # it will give us list.
        return "".join(id)
    
    
    def createaccount(self):
        info = {
            "name": input("Tell your name "),
            "age" : int(input("Tell Age ")),
            "email": input("Tell your email "),
            "pin" : int(input("Tell your 4 number pin ")),
            "accountNo.": Bank.__accountgen(),
            "balance": 0
        }
        
        if info["age"]<18 or len(str(info["pin"])) != 4 :
            print("sorry cannot create bank account.")
        else:
            print("Account has been created successfully.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please check your account number")
            
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN number: "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i["pin"] == pin]
        
        if userdata == False:
            print("Sorry User not found.")
        else:
            amount = int(input("Enter the amont you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much. You can deposit below 10000 and above 0. ")
            else:
                userdata[0]['balance'] += amount        # Here[0] = index of dictionary in list.
                Bank.__update()
                print("Amount deposited successfully. ")

    def withdrawmoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN number: "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i["pin"] == pin]
        
        if userdata == False:
            print("Sorry User not found.")
        else:
            amount = int(input("Enter the amont you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Sorry you don't have much money. ")
            else:
                userdata[0]['balance'] -= amount        # Here[0] = index of dictionary in list.
                Bank.__update()
                print("Amount withdrew successfully. ")

    def showdetails(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN number: "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i["pin"] == pin]
        print("Your information are \n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN number: "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i["pin"] == pin]
        if userdata == False:
            print("No such user exists. ")
        else:
            print("You cannot change age,account number,balance. ")
            print("Fill the details for change or leave it empty if wants no change. ")
            
            newdata = {
                "name": input("Tell your new name or press enter to skip: "),
                "email": input("Tell your new email or press enter to skip: "),
                "pin": input("Tell your new pin or press enter: ")
            }
            
            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            
            newdata["age"] = userdata[0]["age"]
            newdata["accountNo."] = userdata[0]["accountNo."]
            newdata["balance"] = userdata[0]["balance"]
            
            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])
                
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else: 
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Accont details updated successfully. ")
    
    
    def delete(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN number: "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i["pin"] == pin]
        
        if userdata == False:
            print("Sorry no such data exists. ")
        else:
            check = input("Enter y if you actually want to delete or press n if you don't want to delete. ")
            if check == 'n' or check == 'N':
                print("No changes occur.")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully. ")
                Bank.__update()
            
             
            
user = Bank()

print("Enter 1 : Create an account: ")
print("Enter 2 : deposit money: ")
print("Enter 3 : withdrawing money: ")
print("Enter 4 : details account: ")
print("Enter 5 : updating account: ")
print("Enter 6 : Delete account: ")

check = int(input("Tell your response: "))

if check ==1:
    user.createaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.delete()

    
    
    