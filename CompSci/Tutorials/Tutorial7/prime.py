num = int(print("Enter a number: "))
c = 0

while 0<num:
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            break
        divisor += 1