# n = 3
# gg*   n=3; s=1; g=2; i=0
# g***  n=3; s=3; g=3; i=1
#*****  n=3; s=5; g=0; i=2


#  ***  n=3; s=3; g=1
#   *   n=3; s=1; g=2

# top half
n = int(input("Enter number of rows: "))
for row in range(1, n+1):
    print((2 * row) - 1)

#bottom half
#for row in range(row-1, 0, -1):
#   print((n - row) * " " + "*" * (2 * (n-row) - 1))
