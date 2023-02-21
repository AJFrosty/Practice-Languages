import random

num_1 = random.randint(0,100)
num_2 = random.randint(0,100)
answer = int(input(print("What is the sum of", num_1,"and",num_2,"")))

if answer == num_2+num_1 :
    print("Correct")
else:
    print("Incorrect! The answer was", num_1+num_2)