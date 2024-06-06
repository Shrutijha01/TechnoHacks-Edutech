class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your account balance is {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} has been deposited. Your new balance is {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} has been withdrawn. Your new balance is {self.balance}"
        else:
            return "Insufficient"

def main():
    atm = ATM()
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter deposit amount: ₹"))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: ₹"))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using our ATM.Thanks!...")
            break
        else:
            print("Invalid choice. Please choose a valid choice.")

if __name__ == "__main__":
    main()