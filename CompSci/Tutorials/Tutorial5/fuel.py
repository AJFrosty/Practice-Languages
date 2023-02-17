distance = float(input("Please enter the distance needed to travel: "))
miles = float(input("Please enter the fuel efficiency of your vehicle (m/g): "))
price = float(input("Please enter the price per gallon of fuel: "))

cost = round((distance/miles)*price, 2)
print("The cost of driving is ",cost)