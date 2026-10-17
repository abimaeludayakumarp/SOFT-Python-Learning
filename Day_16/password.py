
password = input("Enter your password: ")

if len(password) < 6:
    print("Password is too short")
elif password.isdigit():
    print("Weak password: Use letters and symbols")
elif password.isalpha():
    print("Medium password: Add numbers or symbols")
elif password.isalnum():
    print("Good password: Add special characters")
else:
    print("Strong password")
