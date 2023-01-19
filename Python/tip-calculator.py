#Creating a script to create the tip amount.
cost = input("How much did your food cost? ")
percent = input("What percentage tip do you want to give in tip ")
calc = 0
tip= 0

calc = (float(percent)/100) * float(cost)
tip = calc + float(cost)
print("The tip amount is $" + str(tip))