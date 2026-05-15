#Enter number of days in month: 31
#Enter starting day of the week (1=Sun, 7=Sat): 3

#       1  2  3  4  5
# 6  7  8  9 10 11 12
#13 14 15 16 17 18 19
#20 21 22 23 24 25 26
#27 28 29 30 31

days = int(input("Enter number of days in month: "))
start_day = int(input ("Enter starting day of the week (1=Sun, 7=Sat) "))

#print out spaces based on starting day
for _ in range(start_day - 1):
    print("  ", end="")

#print number of days
for day in range(1, days+1):
    print(f"{day:2}", end="")
    if day % 7 == 0:
        print()
