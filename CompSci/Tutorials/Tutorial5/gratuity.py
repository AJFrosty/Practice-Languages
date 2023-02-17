price = float(input("Please enter the price of your item: "))
perc = float(input("Please enter the percentage gratuity of your item: "))

gratuity = price * perc
total = price + gratuity

print("The price of your item is $",round(price, 2)," and the gratuity of your item is $",round(gratuity, 2)," For a total price of $",round(total, 2))