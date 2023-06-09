class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class AccountManager:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        username = input("Enter a username for your new account: ")
        password = input("Enter a password for your new account: ")
        account = Account(username, password)
        self.accounts.append(account)
        print("Account created successfully!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for account in self.accounts:
            if account.username == username and account.password == password:
                print("Login successful!")
                return

        print("Invalid username or password. Please try again.")

    def switch_account(self):
        username = input("Enter your username: ")

        for account in self.accounts:
            if account.username == username:
                print("Switched to account:", account.username)
                return

        print("Account not found.")


account_manager = AccountManager()

while True:
    print("1. Create Account")
    print("2. Log In")
    print("3. Switch Account")
    print("4. Add Another Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_manager.create_account()
    elif choice == "2":
        account_manager.login()
    elif choice == "3":
        account_manager.switch_account()
    elif choice == "4":
        account_manager.create_account()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
