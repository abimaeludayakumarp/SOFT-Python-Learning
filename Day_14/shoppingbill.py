
item1 = float(input("Enter price of item 1: Rs. "))
item2 = float(input("Enter price of item 2: Rs. "))
item3 = float(input("Enter price of item 3: Rs. "))

total = item1 + item2 + item3

if total >= 2000:
    discount = total * 0.15
elif total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\n----- Shopping Bill -----")
print("Total Amount: Rs.", total)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)
