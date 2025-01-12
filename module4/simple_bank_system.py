class BankAccount:
    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def withdraw(self, amount, password):
        if password == self.password:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Incorrect password.")

    def credit(self, amount,password):
        if password == self.password:
            self.balance += amount
            print(f"Credit successful. New balance: {self.balance}")
        else:
            print("Incorrect password.")

    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")

def main():
    account = BankAccount("123456789", "password123", 1000)

    while True:
        print("\n1. Withdraw Cash")
        print("2. Credit Cash")
        print("3. Change Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to withdraw: "))
            password = input("Enter your password: ")
            account.withdraw(amount, password)
        elif choice == '2':
            amount = float(input("Enter amount to credit: "))
            password = input("Enter your password: ")
            account.credit(amount,password)
        elif choice == '3':
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            account.change_password(old_password, new_password)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()