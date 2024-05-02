# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers."
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)

num=5
result=factorial(num)
print(f"The factorial of {num} is {result}")