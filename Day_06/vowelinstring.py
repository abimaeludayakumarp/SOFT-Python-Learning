text = input("Enter a word: ")
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count = count + 1
print("Number of vowels:", count)