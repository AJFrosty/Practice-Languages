# Prompt the user for input
purchaseAmount = float(input("Enter purchase amount: "))

# Compute sales tax
tax = purchaseAmount * 0.06
#67.2
print("The OG tax is ", tax)
# Display tax amount with two digits after decimal point
print("Sales tax is", int(tax * 100) / 100)