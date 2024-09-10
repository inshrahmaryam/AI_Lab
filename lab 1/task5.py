number = int(input("Enter a number to calculate its factorial: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i 

print(f"The factorial of {number} is {factorial}")
