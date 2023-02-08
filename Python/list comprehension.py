numbers = [1,2,3,4,5,6,7,8,9,10]
##Filter
print(list(filter(lambda num: num%2 ==0, numbers)))

##Map
print(list(map(lambda double: double*2, [1,3,5,7,9])))

##List Comprehension Even Numbers [Filter]
print([num for num in numbers if num%2 ==0])

##Odd Numbers

print([num for num in numbers if num%2 !=0])

##Double [Map]
print([num * 2 for num in numbers])