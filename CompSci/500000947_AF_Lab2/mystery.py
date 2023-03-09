#Write a python program called mystery that should ask you to enter the last digit of your cell phone number and also ask to
#enter your birth year. (Hint: Use the input command but be mindful that the value entered is a string.) n=input(”Enter a
#number: ”) n=int(n)
phone_num= int(input("Enter the last digit of your phone number: "))
year= int(input("Enter your birth year: "))

def mystery(year, phone_num):
    result = phone_num*2
    result = (result+5)*50
    result = result + 1769
    result = result-year
    return result

print(mystery(year,phone_num))