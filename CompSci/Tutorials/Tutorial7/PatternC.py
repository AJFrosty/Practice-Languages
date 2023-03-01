p= 12
for i in range(0, 7):
    for k in range(0,p):
        print(end=" ")
    p=p-2
    for j in range(i,0,-1):
        print(format(j, "2d"), end='')
    print()
    
