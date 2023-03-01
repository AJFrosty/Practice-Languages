nums = int(input("Number of Students: "))
h=s=0

for i in range(1, nums+1):
    grade= float(input("Enter the Student's Grade: "))
    if grade > h:
        s=h
        h=grade
    elif grade>s:
        s = grade
print(f"The highrst grade was {h} and the Second Highest Grade was {s}")