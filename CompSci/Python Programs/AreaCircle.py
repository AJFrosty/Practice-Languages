#Prompt the user to enter a radius 
#radius = float(input("Enter a number for radius: "))
variable=input("Enter radius: ") # accepted as a string
radius=float(variable) #into float
# Compute area (PI*R*R)
area = radius * radius * 3.14159
# Display results
print("The area for the circle of radius", radius, "is", area)

#print(variable)