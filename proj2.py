pin = input("Enter your pin: ")
Balance = int(input("Enter your amount: "))
attempts = 3

while attempts > 0:
    pin_attempt = input("Enter your PIN: ")
    if pin_attempt == pin:
        while True:
            print("\nChoose an option:")
            print("1. Check balance")
            print("2. Withdraw funds")
            print("3. Deposit funds")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                print("Your balance is: $", Balance)
            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: $"))
                if amount > Balance:
                    print("Insufficient funds.")
                else:
                    Balance -= amount
                    print("Withdrawal successful. Remaining balance is: $", Balance)
            elif choice == '3':
                amount = float(input("Enter the amount to deposit: $"))
                Balance += amount
                print("Deposit successful. Current balance is: $", Balance)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect PIN. Please try again. Attempts left:",attempts)