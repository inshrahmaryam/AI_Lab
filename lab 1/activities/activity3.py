isPrime = True
i = 2
n = int(input("Enter a number: "))

while i < n:
    remainder = n % i
    if remainder == 0:
        isPrime = False
        break  
    i += 1  
if isPrime:
    print("The number is prime")
else:
    print("The number is not prime")
