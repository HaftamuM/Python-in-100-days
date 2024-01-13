import random 

print("Hangman: Based on pets names")
print("Guess a letter:")

word_list= ["Dog", "Cat", "Rat"]

#T1 - Randomly choose a word from the word_list and assing it to a variable called chosen_word. 

chosen_word = random.choice(word_list)

#T2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Geuess a letter: ").lower()

#T3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word 

for letter in chosen_word: 
    if letter == guess: 
        print("Right")
    else: 
        print("wrong")