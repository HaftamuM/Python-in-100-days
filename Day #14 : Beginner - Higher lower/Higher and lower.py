from art import logo
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

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b: 
    account_b = random.choice(data)

print(f"compare A: {format_data(account_a)}.")
print(vs)
print(f"compare B: {format_data(account_b)}.")
#Ask the user for a guess

#Chack if a user is correct 
##Get folower count of each account. 
## Use if statement to check if user is correct. 

#Give use feeback on their guess... tracking score 

#Score keeping. 

#Make the game repeatble.

#Making account at posiition B become the next account at Posision A

#CLear the screen betwen round 

