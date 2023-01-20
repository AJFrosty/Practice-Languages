def sum(numbers: list) -> list:
    total = 0
    for i in numbers:
        total = total +i
    return total
print(sum([1,2,3,4,5,6,7,12,34,5,6,7,5,32]))