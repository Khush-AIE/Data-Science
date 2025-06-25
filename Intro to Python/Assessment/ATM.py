class atm:
    print("..........WELCOME..........")
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.create_pin()
        

    def menu(self):
        choice = input('''
            .....Hello There.....
              Select one of the following-->
              Press 1 to change the pin
              Press 2 to deposit money
              Press 3 to withdraw money
              Press 4 to check the balance
              Press 5 to exit
''')
        if choice == '1':
            self.change_pin()
        elif choice == '2':
            self.deposit_money()
        elif choice == '3':
            self.witdr_mny()
        elif choice == '4':
            self.chk_bal()
        else:
            exit
            print("EXITED")

    def create_pin(self):
            user_pin = input("Enter 4 digit number to create pin: ")
            self.pin = user_pin
            print("Your pin has been created")
            self.manddeposit_money()
    def manddeposit_money(self):
        pin = input("Please re enter your pin: ")
        if pin == self.pin:
            amt = int(input("Enter the amount to add in your account: "))
            if amt<1000:
                print("You have to add at least Rs.1000/-")
                self.manddeposit_money()
            else:
                print("TRANSACTION SUCCESSFULL")
                self.balance+=amt
                self.menu()
        else:
            print("INVALID PIN")
            self.manddeposit_money()

    def change_pin(self):
        check = input("Enter existing pin: ")
        if check == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("PIN UPDATED SUCCESSFULLY")
            self.menu()
        else:
            print("INCORRECT PIN")
            self.change_pin()

    def deposit_money(self):
        pin = input("Please re enter your pin: ")
        if pin == self.pin:
            dep_amt = int(input("Enter the amount to deposit: "))
            self.balance+=dep_amt
            print("DEPOSITED")
            self.menu()
        else:
            print("INVALID PIN....ENTER AGAIN")
            self.deposit_money()

    def chk_bal(self):
        pin = input("Please enter your pin: ")
        if pin == self.pin:
            print(f"Your account has balance of Rs.{self.balance}")
            self.menu()

    def witdr_mny(self):
        pin = input("Please enter your pin: ")
        if pin ==  self.pin:
            amt = int(input("Enter amount to withdraw: "))
            if amt>self.balance:
                print("NOT SUFFICIENT BALANCE")
                self.menu()
            elif self.balance-amt<1000:
                print("ALERT YOUR BALANCE IS NOW LESS THAN REQUIRED CHARGES MAY APPLY")
                choice = input("Do you still want to withdraw cash? (YES/NO)-->")
                if choice =='YES' or choice =='yes':
                    print("Here are your cash")
                    self.balance-=amt
                    self.menu()
                else:
                    self.menu()
            else:
                print("HERE ARE YOUR CASH")
                self.balance-=amt
                self.menu()
        else:
            print("INVALID PIN")
            self.menu()
            
        
a = atm()
