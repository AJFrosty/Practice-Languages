num = int(input("Enter a number: "))
n=1
print(f"The factors of {num} are:", end="")
while n<=num:
    if num%n == 0:
        print(n, end=" ")
    n=n+1