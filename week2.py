#1 even or odd checker

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This is even number.")
else: print("Number is odd")

#2. Grade calculator

grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: A-")
elif grade >= 70:
    print("Grade: B")
else :
    print("Grade: C")

#3. Sample Calculator

num_1 = float(input("Enter first number:"))
num_2 = float(input("Enter second number:"))
op = input("Enter operation:")

if op == "+":
    print(num_1+num_2)
elif op == "-":
    print(num_1-num_2)
elif op == "*":
    print(num_1*num_2)
elif op =="/":
    print(num_1/num_2)
else:
    print("Invalid opertion")



count = 1

while (count <= 10):
  print(count)
  count = count + 1
print("Loop is done.")

#for loop
for count in range(11):
    print(count)

#for loop_variable in iterable

#8.Factorial
num = int(input("Enter a number: "))
factorial = 1
for i in  range(1,num + 1):
   factorial = factorial * i
print(factorial)

#Password checker
#open loop
attempt = 0


while attempts < 3:
    temp_pass = "admin123"
    user_pass = input("Enter password ")
    if user_pass == temp_pass:
        print("User validated.")
        break
    else:
        print("Incorrect password")
        attempts = attempts + 1
if attempts == 3:
    print("No more attempts, try again later.")
