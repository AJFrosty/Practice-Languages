a = float(input("Enter the length of edge a: "))
b = float(input("Enter the length of edge b: "))
c = float(input("Enter the length of edge c: "))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print("The perimeter of the triangle is", perimeter)
else:
    print("Invalid")
