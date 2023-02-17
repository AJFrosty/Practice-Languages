invest = float(input("Please enter your monthly investment: "))
rate = float(input("Please enter the interest rate (in the form of a decimal: "))
m_rate = rate/12
filler = 1 + m_rate
total = 0

for _ in range(6):
    total = (100 + total) * filler
print(round(total, 2))
