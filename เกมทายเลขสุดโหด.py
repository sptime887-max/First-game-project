import random

numbers = [random.randint(1, 9)] 

count = 0 
loop = True 

while loop: 
    guess = int(input("Guess a number between 1 and 9: "))
    count += 1 

    if guess in numbers:
        print("Congratulations! You guessed the number.")
        print(f"It took you {count} guesses.")
        loop = False

    elif guess > numbers[0]:
        print("Too high! Try again BABY BOO!")
    else:
        print("Too low! Try again BABY BOO!")