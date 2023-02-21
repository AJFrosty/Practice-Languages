month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year (e.g. 2023): "))

if month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 29
    else:
        days = 28
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 31

month_name = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"][month-1]
print(f"{month_name} {year} has {days} days.")
