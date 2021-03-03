class Bank_Manage():

    def __init__(self, owner, balance):
        self.owner = owner
        self.curr_bal = balance

    def deposit(self):
        val = int(input("Enter amount to be deposited: "))
        self.curr_bal = self.curr_bal + val
        return f"The current balance after deposit is: {self.curr_bal}"

    def withdraw(self):
        val = int(input("Enter amount to be withdrawn: "))
        if val > self.curr_bal:
            print("Funds not available!")
            print(f"The current balance is: {self.curr_bal}. Please enter an amount less than: {self.curr_bal}")
        else:
            self.curr_bal = self.curr_bal - val
            print(f"The current balance after withdraw is: {self.curr_bal}")

    def __str__(self):
        return f"The account holder name is {self.owner} & current balance is {self.curr_bal}"
