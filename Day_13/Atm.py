balance = 5000

print("===== Welcome to ATM =====")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is Rs.", balance)

elif choice == 2:
    amount = float(input("Enter deposit amount: "))
    
    if amount > 0:
        balance = balance + amount
        print("Deposit successful!")
        print("Updated balance: Rs.", balance)
    else:
        print("Invalid amount!")

elif choice == 3:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount!")
    elif amount <= balance:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance: Rs.", balance)
    else:
        print("Insufficient balance!")

else:
    print("Invalid choice!")

