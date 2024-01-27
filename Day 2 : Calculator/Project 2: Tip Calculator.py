# If the bill was $150.00  splt between 5 peopl, with 12% tip.
# Each Person should pay(150.00/5) * 1.12 = 33.6
# Round the result to 2 decmal places = 33.60 

Tip_rate = 1.12 # we already assigned the tip variable 

print("Hello Welcome to the Tip Calculator!!\n")
Total_Bill = int(input("Total Expense : "))
Number_People = int(input("Numer of People : "))
Tip = (Total_Bill / Number_People) * Tip_rate 
 
print("Each Person Pays: ", Tip)
