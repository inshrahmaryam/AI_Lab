number = input("Please enter an integer: ")
if number[0] == '-':
    # Reverse the digits after the minus sign
    reversed_number = '-' + number[:0:-1]
else:
    # Reverse the number
    reversed_number = number[::-1]
print("The reversed number is:", reversed_number)
