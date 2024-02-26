from art import logo, vs
from game_data import data 
import random 


# Display art  from art.py 
## Generate a radom account from the game data. 
def format_data (account): 
    """""#Format the account data into printable - dictionaries are accessed through a key"""""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer (guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers: 
        return guess == "a"
    else: 
        return guess == "b"
    

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #Generate a random account from the game data. 

    #Making account at posision B become the next account at posisition A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choce(data)

    print(f"compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    #Ask the user for a guess
    guess = input("who has more followers? Type 'A' or 'B': ").lower()
    #Check  if a user is correct 
    ##Get folower count of each account. 
    a_follower_count = account_a["follower_count"] # retreving the follower-Count
    b_follower_count = account_b["follower_count"] # retreving the follower-Count
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Give use feeback on their guess... tracking score 
    ##Score keeping. 
    if is_correct:
        score += 1
        print("you are right: your score: {score}.")
    else:
        game_should_continue == False
        print("Sorry, you lost: you score: {score}.")
    
    #Make the game repeatble.

#Making account at posiition B become the next account at Posision A

#CLear the screen betwen round 

