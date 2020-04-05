def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("enter a number to compute the factiorial : "))
print(factorial(n))
