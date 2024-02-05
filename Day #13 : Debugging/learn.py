#code 1 - logical error 
# def my_function(): 
  #  for i in range(1, 20):
   #     if i == 20: # change the value of i == 21 it works
    #        print("you got it")

# my_function()

#code 2 - 

from random import randint 

dice_imgs = ["1", "2", "3", "4"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
