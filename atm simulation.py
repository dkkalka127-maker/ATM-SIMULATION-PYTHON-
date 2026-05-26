balance = 1000.00
pin = "1234"
is_running = True

print("=== WELCOME TO THE SIMPLE ATM ===")

entered_pin = input("Please enter your 4-digit PIN: ")

if entered_pin == pin:
    while is_running:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            print(f"Your current balance is: ₹{balance:.2f}")
            
        elif choice == "2":
            deposit_amount = float(input("Enter amount to deposit (₹): "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"₹{deposit_amount:.2f} deposited successfully.")
            else:
                print("Invalid amount. Please enter a positive number.")
                
        elif choice == "3":
            withdraw_amount = float(input("Enter amount to withdraw (₹): "))
            if withdraw_amount > balance:
                print("Insufficient funds! Transaction cancelled.")
            elif withdraw_amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                balance -= withdraw_amount
                print(f"₹{withdraw_amount:.2f} withdrawn successfully.")
                
        elif choice == "4":
            print("Thank you for using our banking services. Goodbye!")
            is_running = False
        else:
            print("Invalid choice. Please select a valid option (1-4).")
else:
    print("Incorrect PIN. Access Denied.")