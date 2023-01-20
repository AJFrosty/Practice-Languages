input1 = input("What is your name: ")
input2= input("What is your age: ")
input3= input("What is your favorite color: ")

def introduction():
    person = {
        'name' : input1,
        'age' : int(input2),
        'color': input3
    }
    print(f"My name is {person['name']}, I am {person['age']} Old and my favorite color is {person['color']} ")
introduction()