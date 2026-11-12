numbers = [12, 45, 23, 67, 34]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)