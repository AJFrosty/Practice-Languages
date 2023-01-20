fruits = ['apples', 'oranges', 'banana', 2, 8.7, "mood"]
#Adding to a list
fruits.append("stawberry")
fruits.append("kiwi")
print(fruits)

#Indexing
print(fruits[0])
print(fruits[4])

#Last Item
print(fruits[-1])

#Slicing - Range (0(Inclusive) to 3(Exclusive))
print(fruits[0:3])

#Length
print(len(fruits))
print(fruits[0:len(fruits)-1])

#Slicing Strings
name= "Frosty"
print(name[0:4])

#Stepping in Arrays (From:To:Step By)
print(fruits[0:len(fruits):2])
#Reverse 
print(fruits[::-1])