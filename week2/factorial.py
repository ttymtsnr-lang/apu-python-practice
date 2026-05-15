def factorial(n: int):
    if n == 0:
        return 1
    return n * factorial(n-1)

# factorial(5)
# retrun 5 * 4 factorial(4)
# retrun 5 * 4 * 3 factorial(2)
# retrun 5 * 4 * 3 * 2 factorial(1)
# retrun 5 * 4 * 3 * 2 * 1 factorial(0)
# retrun 5 * 4 * 3 * 2 * 1 * 1

print(factorial(5))
