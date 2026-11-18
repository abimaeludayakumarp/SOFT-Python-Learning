
def find_common(a, b):
    return list(set(a) & set(b))

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70, 80]

print("Common Elements:", find_common(list1, list2))
