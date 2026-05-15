def celsius_to_fahrenheit(c):
    return (9/5) * c + 32
temps = [10, 20, 30]

for t in temps:
    print(celsius_to_fahrenheit(t))

def find_largest(a, b, c):
    return max(a, b, c)

First_largest = int(input("Please enter first number: "))
Second_largest = int(input("Please enter second number: "))
Third_largest = int(input("Please enter third number: "))

print("Largest:", find_largest(First_largest, Second_largest, Third_largest))

def multiples(n, limit):
    i = 1
    num = 0
    while True:
        num = n * 1
        if num > limit:
            break
        print("The number for now is : ", num)
        i += 1

n = int(input("Please enter the number"))
limit = int(input("Please enter the limit for multiply"))

multiples(n, limit)
