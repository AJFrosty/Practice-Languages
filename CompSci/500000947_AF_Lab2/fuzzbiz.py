# python program called fuzzbiz, which takes a number as input. If the number is divisible by 3 return the string
#“Fuzz”, if the number is divisible by 5 return the string “Biz” and if the number is divisible by both numbers then return the
#string “FuzzBiz”. If it is only any of the above cases then the program should return “No Fuzz No Biz”.

def fuzzbiz(num):
    if num%5 == 0 and num%3==0:
        print("Fuzzbiz")
    elif num%5==0:
        print("Biz")
    elif num%3==0:
        print("Fuzz")
    else:
        print("No Fuzz No Biz")
