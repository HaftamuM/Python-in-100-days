from art import logo, vs
from game_data import data 
import random 

# Display art  from art.py 

print(logo)
# Generate a radom account from the game data. 
def format_data (account): 
    """""#Format the account data into printable - dictionaries are accessed through a key"""""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer (guess, a_followers, b_followers):
    """Use if statement to check """
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b: 
    account_b = random.choice(data)

print(f"compare A: {format_data(account_a)}.")
print(vs)
print(f"Against B: {format_data(account_b)}.")

      
#Ask the user for a guess
guess = input("who has more followers? Type 'A' or 'B': ").lower()
#Chack if a user is correct 
##Get folower count of each account. 
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

## Use if statement to check if user is correct. 

#Give use feeback on their guess... tracking score 

#Score keeping. 

#Make the game repeatble.

#Making account at posiition B become the next account at Posision A

#CLear the screen betwen round 

