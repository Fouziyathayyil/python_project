#Write a python program to replicate a Banking system. The following features are mandatory:
#1.Account login
#2. Amount Depositing
#3. Amount Withdrawal"""
class BankAccount:#serve as blueprint for individual bank accounts
    def __init__(self,Account_number,Account_holder,Username,Password,Balance=0):
        self.Account_number=Account_number
        self.Account_holder=Account_holder
        self.Balance=Balance
        self.Username=Username
        self.Password=Password
    def login(self):
        Ac_num=int(input("enter your account number : "))
        entered_username=input("enter your user name : ")
        entered_password=input("enter your password : ")
        if Ac_num==self.Account_number and entered_username==self.Username and entered_password==self.Password:
            print(f"Welcome, {self.Account_holder}")
            while True:
             print("press '1' for deposit")
             print("press '2' for withdraw")
             print("press '3' for check balance")
             print("press '0' to logout")
             option = int(input("enter your choice : "))
             if option == 1:
                Account1.deposit()
             elif option == 2:
                Account1.withdrawel()
             elif option == 3:
                Account1.balance_check()
             elif option==0:
                 print("Logged out")
                 break
             else:
                print("please enter a valid option")
        else:
            print("Login failed. Please check your credentials")
    def deposit(self):
        amount=int(input("enter the amount to be deposit : "))
        self.Balance+=amount
        print(f"An amount of {amount} has credited to your account")
    def withdrawel(self):
        amount=int(input("enter the amount for withdraw : "))
        if self.Balance>=amount:
            print(f"{amount} has been withdrawed")
            self.Balance-=amount
        else:
            print("you have no sufficient balance to withdraw")
    def balance_check(self):
        print(f"your balance is {self.Balance}")
Account1=BankAccount(12345,"John","john123","password123")
Account1.login()