

balance = 5000  # Initial balance
pin = "1234"    # Initial PIN
max_attempts = 3  # Maximum allowed attempts for password
transactions = []  # List to store transactions

while True:
    username = input("Enter username: ")
    if username == "ashish@123":
        attempts = 0  # Initialize attempts counter

        while attempts < max_attempts:  # Limit password attempts
            password = input("Enter password: ")

            # Check if the password is numeric and has exactly 4 digits
            if not (password.isdigit() and len(password) == 4):
                print("Invalid password. It must contain only numbers (0-9) and be exactly 4 digits.")
                attempts += 1
                if attempts == max_attempts:
                    print("Too many failed attempts. Your account is frozen.")
                    exit()  # End the program
                else:
                    print(f"Attempt {attempts}/{max_attempts}. Try again.")
                continue  # Go to the next attempt

            if password == pin:  # Check against the current PIN (new PIN will be recognized)
                print("Welcome! What would you like to do?")
                print("a) Balance check\nb) Deposit amount\nc) Withdraw amount\nd) Change PIN\ne) Exit\nf) Mini Statement")

                choice = input("Press: ").lower()

                if choice == "a":  # Balance check
                    next_account = input("a) Current Account\nb) Saving Account\nc) Credit Card\n Press: ")
                    if next_account == "a":
                        print("You don't have a current account.")
                    elif next_account == "b":
                        print(f"Your balance is: {balance}")
                    elif next_account == "c":
                        print("You don't have any credit card.")
                    else:
                        print("Invalid option.")
                    next_action = input("a) Exit\nb) Continue\nPress: ").lower()
                    if next_action == "a":
                        print("Thank you")
                        exit()  # End the program
                    elif next_action == "b":
                        continue
                    else:
                        print("Invalid option.")

                elif choice == "b":  # Deposit amount
                    next_account = input("a) Current Account\nb) Saving Account\nc) Credit Card\n Press: ")
                    if next_account == "a":
                        print("You don't have a current account.")
                    elif next_account == "b":
                        deposit_amount = input("How much would you like to deposit: ")

                        # Validate if deposit amount is numeric
                        if not deposit_amount.isdigit():
                            print("Invalid input. Please enter a numeric value for deposit.")
                            continue

                        deposit_amount = int(deposit_amount)  # Convert to integer

                        if deposit_amount <= 0:  # Check if deposit amount is positive
                            print("Invalid amount. You cannot deposit a negative or zero value.")
                        else:
                            balance += deposit_amount
                            transactions.append(f"Deposited: {deposit_amount}")  # Log the transaction
                            print(f"Your new balance is: {balance}")
                        next_action = input("a) Exit\nb) Continue\n Press: ").lower()
                        if next_action == "a":
                            print("Thank you")
                            exit()  # End the program
                        elif next_action == "b":
                            continue
                        else:
                            print("Invalid option.")
                    elif next_account == "c":
                        print("You don't have any credit card.")
                    else:
                        print("Invalid option.")

                elif choice == "c":  # Withdraw amount
                    next_account = input("a) Current Account\nb) Saving Account\nc) Credit Card\n Press: ")
                    if next_account == "a":
                        print("You don't have a current account.")
                    elif next_account == "b":
                        withdraw_amount = input("How much would you like to withdraw: ")

                        # Validate if withdraw amount is numeric
                        if not withdraw_amount.isdigit():
                            print("Invalid input. Please enter a numeric value for withdrawal.")
                            continue

                        withdraw_amount = int(withdraw_amount)  # Convert to integer

                        if withdraw_amount > balance:
                            print("Insufficient funds.")
                        else:
                            balance -= withdraw_amount
                            transactions.append(f"Withdrew: {withdraw_amount}")  # Log the transaction
                            print(f"Your new balance is: {balance}")
                        next_action = input("a) Exit\nb) Continue\n Press: ").lower()
                        if next_action == "a":
                            print("Thank you")
                            exit()  # End the program
                        elif next_action == "b":
                            continue
                        else:
                            print("Invalid option.")
                    elif next_account == "c":
                        print("You don't have any credit card.")
                    else:
                        print("Invalid option.")

                elif choice == "d":  # Change PIN
                    next_account = input("a) Current Account\nb) Saving Account\nc) Credit Card\n Press: ")
                    if next_account == "a":
                        print("You don't have a current account.")
                    elif next_account == "b":
                        old_pin = input("Enter your old PIN: ")
                        if old_pin == pin:  # Verify the old PIN
                            new_pin = input("Enter new PIN: ")

                            # Validate new PIN (numeric and length 4)
                            if not (new_pin.isdigit() and len(new_pin) == 4):
                                print("Invalid PIN. It must contain only numbers (0-9) and be exactly 4 digits.")
                                continue  # Return to the PIN change section if invalid

                            # Check if the new PIN is the same as the old PIN
                            if new_pin == pin:
                                print("New PIN cannot be the same as the old PIN. Please choose a different PIN.")
                                continue  # Ask user to re-enter the new PIN

                            confirm_pin = input("Confirm new PIN: ")
                            if new_pin == confirm_pin:
                                pin = new_pin  # Set the new PIN
                                print("Your PIN has been successfully changed.")
                                next_action = input("a) Exit\nb) Continue\nPress: ").lower()
                                if next_action == "a":
                                    print("Thank you")
                                    exit()  # End the program
                                elif next_action == "b":
                                    continue  # Continue with the new PIN in effect
                                else:
                                    print("Invalid option.")
                            else:
                                print("Pins do not match. Try again.")
                        else:
                            print("Incorrect old PIN. Try again.")
                    elif next_account == "c":
                        print("You don't have any credit card.")
                    else:
                        print("Invalid option.")

                elif choice == "e":  # Exit
                    print("Thank you")
                    exit()  # End the program

                elif choice == "f":  # Mini Statement
                    next_account = input("a) Current Account\nb) Saving Account\nc) Credit Card\n Press: ")
                    if next_account == "a":
                        print("You don't have a current account.")
                    elif next_account == "b":
                        print("Mini Statement (Last 5 Transactions):\n")
                        # Show the last 5 transactions
                        for transaction in transactions[-5:]:
                            print(transaction)
                        next_action = input("a) Exit\nb) Continue\nPress: ").lower()
                        if next_action == "a":
                            print("Thank you")
                            exit()  # End the program
                        elif next_action == "b":
                            continue
                        else:
                            print("Invalid option.")
                    elif next_account == "c":
                        print("You don't have any credit card.")
                    else:
                        print("Invalid option.")

                else:
                    print("Please enter a correct option.")
            else:
                print("Incorrect password.")
                attempts += 1
                if attempts == max_attempts:
                    print("Too many failed attempts. Your account is frozen.")
                    exit()  # End the program
                else:
                    print(f"Attempt {attempts}/{max_attempts}. Try again.")
    else:
        print("Incorrect username. Try again.")
