#TODO1 Print report 
#TODO2 Check Resource Sufficent 
#TODO3 Process coins 
#TODO4 Check transaction sucessful
#TODO5 Make coffee

from menu import Menu, MenuItem 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True 

#create a new object 
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#Step 1 : call the report method to print the report 
#Calling the method within the object 
coffee_maker.report() 
money_machine.report()

#Step 2 : Check the resources sufficient? 
while is_on: 
    options = menu.get_items()
    choice = input(f"What do you like?({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        drink = menu.find_drink(choice)
        print(coffee_maker.is_resource_sufficient(drink))
       #step 3 : Process coins 
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink,cost):
            coffee_maker.make_coffee(drink)
            


        