class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ {amount} deposited successfully!")
        else:
            print("❌ Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
        elif amount > self.__balance:
            print("❌ Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"💸 {amount} withdrawn successfully!")

    def check_balance(self):
        print(f"💰 Current balance: {self.__balance}")

    def account_info(self):
        print(f"👤 Owner: {self.owner_name}")
        print(f"💵 Balance: {self.__balance}")

        
def main():
    print("🏦 Welcome to the Bank Account System 🏦")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Info")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            account.check_balance()

        elif choice == '4':
            account.account_info()

        elif choice == '5':
            print("👋 Thank you for using our bank system!")
            break

        else:
            print("❌ Invalid option, please try again!")


if __name__ == "__main__":
    main()