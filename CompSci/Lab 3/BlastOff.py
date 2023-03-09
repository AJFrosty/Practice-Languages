count = int(input("Enter a number: "))
iteration = int(input("How much to decrease by?: "))
while count>0:
    if count%2 == 0:
        print(f"{count} is Even")
    else:
        print(f"{count} is Odd")
    count=count-iteration
print("Blastoff!!")