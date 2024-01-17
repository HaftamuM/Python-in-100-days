import random 

print("Hangman: Based on pets names")

word_list= ["Dog","Cat","Rat"]

#T1 - Randomly choose a word from the word_list and assing it to a variable called chosen_word. 

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length): 
    display +="_"
print(display)

end_of_game = False

while not end_of_game: 
    #T2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ")


    #T3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word 

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess: 
            display[position] = letter
    print(display)
    ## print(f"{''.join(display)}")

if "_" not in display: 
    end_of_game = True
    print("you win.")

#T4 - Use a while loop to let the user guess again and check if the gammer won 

