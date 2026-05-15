days = int(input("Enter number of days in montah: "))
start = int(input("Enter starting day of the week(1=Sunday, 7=Saturday): "))

for i in range(1, days+1):
    if i % 7 != 0:
        print(" " * (start-1) + str(i))
