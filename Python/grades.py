grade = input("What grade did you receive? ")
percent = float(grade)

if percent >= 90:
    print("Grade A with a",percent)
elif percent >= 80:
    print("Grade B with a", percent)
elif percent >= 70:
    print("Grade C with a", percent)
elif percent >= 60:
    print("Grade D with a", percent)
else:
    print("Grade F with a", percent)

if(percent>=60):
    print("You're Passing")
else:
    print("You're Failing!!!")