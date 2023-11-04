for i in range(6,0,-2):
    for j in range(6-i,0,-2):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print("*",end=" ")
    print()
print(5*" ",end="")
print("*")
for i in range(2,7,2):
    for j in range(2-i+4,0,-2):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()
