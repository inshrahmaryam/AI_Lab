numbers = input("Enter a set of integers separated by spaces: ").split()

# Convert each input number from string to integer
numbers = [int(num) for num in numbers]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num  
    else:
        odd_sum += num   


print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
