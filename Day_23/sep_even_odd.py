numbers = [12, 7, 9, 20, 34, 15]

even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]

print("Even:", even)
print("Odd:", odd)