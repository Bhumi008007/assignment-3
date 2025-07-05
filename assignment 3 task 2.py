import math

# Ask the user for a number
try:
    number = float(input("Enter a number: "))

    # Calculate square root
    if number >= 0:
        sqrt_result = math.sqrt(number)
    else:
        sqrt_result = "Undefined for negative numbers"

    # Calculate natural logarithm
    if number > 0:
        log_result = math.log(number)
    else:
        log_result = "Undefined for zero or negative numbers"

    # Calculate sine (in radians)
    sine_result = math.sin(number)

    # Display the results
    print(f"\nResults for number: {number}")
    print(f"Square Root: {sqrt_result}")
    print(f"Natural Logarithm (ln): {log_result}")
    print(f"Sine (in radians): {sine_result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
