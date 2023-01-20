def max(numbers: list) -> list:
    maximum = 0
    for i in numbers:
        if i>maximum:
            maximum = i
    return maximum
print(max([1,2,3,4,5,6,7,8,76,54,3,212,45]))
