terms = int(input("How many terms of the Fibonacci series do you want? "))

first = 0
second = 1

print(first, end=" ")

for i in range(1, terms):  # We already printed the first term, so we start from 1
    print(second, end=" ")
    next_term = first + second  
    first = second  
    second = next_term  
