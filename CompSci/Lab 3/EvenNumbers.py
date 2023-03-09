num1 = int(input("Enter the lower number: "))
num2 = int(input("Enter the higher number: "))
print(f"The even numbers between {num1} and {num2} are: ", end=" ")

while num1<=num2:
    if num1%2 == 0:
        print(num1, end=" ")
    num1=num1+1