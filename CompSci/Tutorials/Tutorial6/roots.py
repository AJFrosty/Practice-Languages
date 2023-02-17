a,b,c = eval((input("Enter the coefficients of the Equation: ")))

sqrt= (b**2)- (4*a*c)
if sqrt >= 0:
    r1 = ((-1*b) + (sqrt)**(1/2))/(2*a)
    r2 = ((-1*b) - (sqrt)**(1/2))/(2*a)
    if r1 == r2:
        print("This is a double root")
        print("Coefficient of x^2 is",a,"Coefficient of x is",b," and the Y intercept is",c)
        print("The roots of the quadratic are:", r1)
    else:
        print("Coefficient of x^2 is",a,"Coefficient of x is",b," and the Y intercept is",c)
        print("The roots of the quadratic are:", r1,r2)
else:
    print("This equation has no real roots!!!!")


