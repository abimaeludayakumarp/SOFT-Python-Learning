maths = int(input("Enter Maths mark: "))
python = int(input("Enter Python mark: "))
cpp = int(input("Enter C++ mark: "))
english = int(input("Enter English mark: "))
management = int(input("Enter Management mark: "))

total = maths + python + cpp + english + management
percentage = total / 5

print("Total =", total)
print("Percentage =", percentage)

if percentage >= 90:
    print("Grade A+")
elif percentage >= 80:
    print("Grade A")
elif percentage >= 70:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
else:
    print("Fail")