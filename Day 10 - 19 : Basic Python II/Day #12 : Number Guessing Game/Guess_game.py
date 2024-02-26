# final project guessing game 
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10 
HARD_LEVEL_TURNS = 5
print("Welcome to the number Guessing Game!")

# step 2 : create a function for a user's guess against actual answer.
def check_answer(guess, answer) :
    if guess > answer: 
        print("Too high")
    elif guess < answer: 
        print("Too .")
    else: 
        print(f"you got it! The answer was {answer}.")


def set_diffculty(): 
    level = input("choose a diffculty. Type 'easy' or 'hard':")
    if level  == 'easy': 
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Step 0 : choosing random number between 0 and 100 

print("Welcome to the number Guessing game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1, 100)
# step 1 : get the input from the user 

turns = set_diffculty()

Guess = int(input("Make a guess:"))

# step 4 : track and number of turns and reduce by 1 (loop)
print(f"you have {turns} attemps remaining to guess the number.")

# step 3 : Check if the guess is equal, less or greater of the answer

print("Choose a diffculty.Type 'Easy' and 'Hard'")



