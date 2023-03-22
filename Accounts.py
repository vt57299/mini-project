'''.) Bank Account Manager - Create a class called Account which will be an abstract class for three other classes called
 CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.'''

from abc import abstractmethod,ABC

class Account(ABC):
    def __init__(self,owner_name,balance = 0):
        self.owner = owner_name
        self.balance = balance
    
    @abstractmethod
    def deposite(self,amount):         
        pass
    
    @abstractmethod
    def withdraw(self,amount):        
        pass

    def __str__(self):
        print(f"\nOwner name: {self.owner}\nAccount balance: {self.balance}")

class CheckingAccount(Account):
    def __init__(self, owner_name, balance=0):
        super().__init__(owner_name, balance)

    def deposite(self, amount):
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if self.balance - amount <0:
            print("\nInsufficient Balnance!")
            return False
        else:
            self.balance = self.balance - amount
            return True
        
    def __str__(self):
        print(f"\nOwner name: {self.owner}\nAccount balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, owner_name, balance=0):
        super().__init__(owner_name, balance)
    
    def deposite(self, amount):
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if self.balance - amount < 3000:
            print("\nYou cannot exceed your minimum Account Balance required!!!")
            return False
        else:
            self.balance = self.balance - amount
            return True
    
    def __str__(self):
        print(f"\nOwner name: {self.owner}\nAccount balance: {self.balance}")

class BusinessAccount(Account):
    def __init__(self, owner_name, balance=0):
        super().__init__(owner_name, balance)
    
    def deposite(self, amount):
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if self.balance - amount <10000:
            print("\nYou cannot exceed your minimum Account Balance required!!!")
            return False
        else:
            self.balance = self.balance - amount
            return True
    
    def __str__(self):
        print(f"\nOwner name: {self.owner}\nAccount balance: {self.balance}")


def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False
    

if __name__ == "__main__":
    pin = input("Enter four digit pin: ")
    if verify_pin(pin):
        print("\n-------Login successfull-------")

        while True:
            print("\n------Main Menu------")
            main_choice =  int(input("\n1.Checking Account\n2.Savings Account\n3.Business Account\n4.Exit\nEnter choice: "))
            if main_choice == 1:
                checking = CheckingAccount("Demo1",10000)
                print("\n---------Checking Account---------")

                while True:
                    choice = int(input("\n1. Deposite\n2. withdraw\n3. mini statement\n4. Return to main menu\n5. Exit.\nEnter choice: "))
                    if choice == 1:
                        amount = int(input("\nEnter Depositing amount: "))
                        flag = checking.deposite(amount)
                        if flag:
                            print(f"\n{amount}rs. has been successfully deposited to your account.")
                            
                        else:
                            print(f"\nCannot deposite {amount} to your Account!!")
                            
                    elif choice == 2:
                        amount = int(input("\nEnter withdrawal amount: "))
                        flag = checking.withdraw(amount)
                        if flag:
                            print(f"\nYou have withdraw {amount}rs from your account")
                            print()
                            print(f"\nYour remaining Account Balance is {checking.balance}rs.")
                            
                        else:
                            print(f"\nWithdraw Unsucessfull!!")
                            
                    elif choice == 3:
                        print("-----Mini Statement-----")
                        checking.__str__()
                       

                    elif choice == 4:
                        break

                    elif choice == 5:
                        print("\nThank you for using our ATM. See you next time!!!")
                        exit()
                    else:
                        print("\n------Please enter correct input!!------")

            elif main_choice == 2:
                savings = SavingsAccount("Demo2",25000)
                print("\n---------Savings Account---------")
                while True:
                    choice = int(input("\n1. Deposite\n2. withdraw\n3. mini statement\n4. Return to main menu\n5. Exit.\nEnter choice: "))
                    if choice == 1:
                        amount = int(input("\nEnter Depositing amount: "))
                        flag = savings.deposite(amount)
                        if flag:
                            print(f"\n{amount}rs. has been successfully deposited to your Savings account.")
                            
                        else:
                            print(f"\nCannot deposite {amount} to your Account!!")
                            
                    elif choice == 2:
                        amount = int(input("\nEnter withdrawal amount: "))
                        flag = savings.withdraw(amount)
                        if flag:
                            print(f"\nYou have withdraw {amount}rs from your account")
                            print()
                            print(f"\nYour remaining Account Balance is {savings.balance}rs.")
                            
                        else:
                            print(f"\nWithdraw Unsucessfull!!")
                            
                    elif choice == 3:
                        print("-----Mini Statement-----")
                        savings.__str__()

                    elif choice == 4:
                        break

                    elif choice == 5:
                        print("\nThank you for using our ATM. See you next time!!!")
                        exit()
                    else:
                        print("\n------Please enter correct input!!------")

            elif main_choice == 3:
                business = BusinessAccount("Demo3",50000)
                print("\n---------Business Account---------")
                while True:
                    choice = int(input("\n1. Deposite\n2. withdraw\n3. mini statement\n4. Return to main menu\n5. Exit.\nEnter choice: "))
                    if choice == 1:
                        amount = int(input("\nEnter Depositing amount: "))
                        flag = business.deposite(amount)
                        if flag:
                            print(f"\n{amount}rs. has been successfully deposited to your Savings account.")
                            
                        else:
                            print(f"\nCannot deposite {amount} to your Account!!")
                            
                    elif choice == 2:
                        amount = int(input("\nEnter withdrawal amount: "))
                        flag = business.withdraw(amount)
                        if flag:
                            print(f"\nYou have withdraw {amount}rs from your account")
                            print()
                            print(f"\nYour remaining Account Balance is {business.balance}rs.")
                            
                        else:
                            print(f"\nWithdraw Unsucessfull!!")
                            
                    elif choice == 3:
                        print("-----Mini Statement-----")
                        business.__str__()

                    elif choice == 4:
                        break

                    elif choice == 5:
                        print("\nThank you for using our ATM. See you next time!!!")
                        exit()
                    else:
                        print("\n------Please enter correct input!!------")

            elif main_choice == 4:
                print("\nThank you for using our ATM. See you next time!!!")
                exit()

            else:
                print("\n------Please enter correct choice------")
    else:
        print("\nYou have entered wrong pin!!!")

# Pin = 1234 <----------