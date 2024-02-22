#code 1 - logical error 
# solution - 
# def my_function(): 
  #  for i in range(1, 20):
   #     if i == 20: # change the value of i == 21 it works
    #        print("you got it")

# my_function()

#code 2 - error for spectific result the array value isn't the same as the given array

# from random import randint 
# dice_imgs = ["1", "2", "3", "4"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# code 3 - logic error ( solution: read the line one by one)
year = int(input("What's your year of birth "))
if year > 1989 and year < 1994:
      print("You are a millenial.")
elif year > 1984: 
      print("you are a Gen z")

