# program requiremnt - follow the coffee machine 
#: 1. print report
#: 2. check resources sufficient? 
# : 3. Process using a cone 
# : 4. Check tranaction sucessful?
# : 5.Make the coffe

MENU = { 
    "espresso": {
        "ingredients":{
        "water":50,
        "coffee":18,
     },
     "cost": 1.5,
},
    "Latte": {
        "ingredients":{
        "water":200,
        "milk":150,
        "coffee":24,
     },
     "cost": 1.5,
},
    "caooaccino": {
        "ingredients":{
        "water":200,
        "milk":150,
        "coffee":24,
     },
     "cost": 3.0,
}}
profit = 0
resources = { 
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingrediants):
    """Returns True when order can be made.  """

    for item in order_ingrediants: 
        if order_ingrediants[item] >= resources[item]:
            print("Sorry there isn't enough {item}.")
            return False
        return True

def process_coins(): 
    """Rteurn the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How may QUarters?:")) * 0.25
    total += int(input("How may dimes?:")) * 0.1
    total += int(input("How may nickles?:")) * 0.05
    total += int(input("How may pannies?:")) * 0.01
    return True

def is_transaction_sucessful(money_receivd,drink_cost):
    if money_received >= drink_cost: 
        change = round(money_receivd - drink_cost, 2) 
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost:
        return True 
    else: 
        print("SOrry that is not engh money.Money rerfunded.")
        return False 
    
def mmake_coffee(drink_name, order_ingrediants):
    for item in order_ingrediants: 
        resource[item] -= order_ingrediants{item]}
        print(f"Here is your {drink_name} ")
is_on = True 


while is_on: 
    choice = input ("What would you like? (espresso/latte/Cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"water:{resources ['water']}ml")
        print(f"Milk:{resources ['milk']}ml")
        print(f"coffee:{resources ['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingrediants"]):
            payment = process_coins()
            if is_transaction_sucessful(payment,drink["cost"]):
                mak_coffee(choice, drink["ingrediants"])