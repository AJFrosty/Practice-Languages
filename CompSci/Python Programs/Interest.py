int_rate= float(input("Please enter the monthly interest rate: "))
num_years= float(input("Please input the number of years you have to pay off the loan: "))
loan_amt = float(input("Please enter the loan ammount "))

month_pay = (loan_amt*int_rate)/(1-(1/(1+int_rate)**(num_years*12)))
total = month_pay*12*num_years

print("Monthly payment is: $",month_pay)
print("Total payment is: $", total)