import random

def guess_the_number():
    print("Welcome to the Number Guessing game!")

    secret_number = random.randint(1,20)
    attempts = 0

    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt{attempts + 1}: Guess a number between 1 to 20: "))

            attempts += 1
              
            if guess < 1 or guess > 20:
                print("Please guess a number *within* range!")  

            elif guess < secret_number:
                print("Too high! Try again")    

            elif guess > secret_number:
                print("Too high! Try again")  

            else: print(f"Congratulation! You guessed it in {attempts} attempts.")       


        except ValueError:
         print("Please enter a valid number")

    if guess != secret_number:
        print(f"Game over! The correct number was {secret_number}.")     

guess_the_number()        



