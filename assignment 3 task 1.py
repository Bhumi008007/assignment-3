
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


sample_number = 5
result = factorial(sample_number)

print(f"The factorial of {sample_number} is: {result}")
