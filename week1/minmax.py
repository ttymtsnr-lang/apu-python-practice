a = int(input("Enter integer"))
b = int(input("Enter integer"))
c = int(input("Enter integer: "))
d = int(input("Enter integer"))

#first pair
if a > b:
    max1 = a
    min1 = b
else:
    max1 = b
    min1 = a

#seconf pair
if c > d:
    max2 = c
    min2 = d
else:
    max2 = d
    min2 = c

#compare two maxes
if max1 > max2:
    largest = max1
else:
    largest = max2

#compare two mins
if min1 < min2:
    smallest = min1
else:
    smallest = min2

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
