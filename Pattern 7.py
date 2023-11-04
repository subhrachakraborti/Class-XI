for i in range(5,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(5,i-1,-1):
        print("*",end=" ")
    print()
for i in range(4,0,-1):
    for l in range(5,i,-1):
        print(" ",end=" ")
    for m in range(1,i+1):
        print("*",end=" ")
    print()
