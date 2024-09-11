import random
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
TRY = 0
RUNNING = True

print("Alright...")

while RUNNING:
    GUESS = input("What is your lucky number? (type 'exit' to quit): ")
    
    if GUESS.lower() == "exit":
        print("Better luck next time.")
        RUNNING = False
        break
    
    try:
        GUESS = int(GUESS)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    TRY += 1  # Incrementing TRY after each guess
    
    if GUESS < NUMBER:
        print("Wrong, too low.")
    elif GUESS > NUMBER:
        print("Wrong, too high.")
    elif GUESS == NUMBER:
        print(f"Yes, that's the one, {NUMBER}.")
        
        if TRY < 2:
            print(f"Impressive, only {TRY} try.")
        elif TRY >= 2 and TRY < 10:
            print(f"Pretty good, {TRY} tries.")
        else:
            print(f"Bad, {TRY} tries.")
        
        RUNNING = False
