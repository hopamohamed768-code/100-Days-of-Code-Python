import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

the_guess = random.randint(1, 100)

the_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def play_game(attempts_num):

    for attempts in range(attempts_num):
        print(f"You have {attempts_num - attempts} attempts remaining to guess the number.")
        num = int(input("Guess Number: "))
        if num == the_guess:
            print("You win")
            return
        elif num < the_guess:
            print("too low")
        elif num > the_guess:
            print("too high")
    print("You've run out of guesses, you lose.")
    print(f"The correct number was: {the_guess}")



if the_difficulty == 'easy':
    play_game(10)
elif the_difficulty == 'hard':
    play_game(5)
else:
    print("Write the right word")



