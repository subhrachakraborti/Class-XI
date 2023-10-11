x=0
for i in range(5,0,-1):
    for j in range(0,x):
        print(" ",end=" ")
    x+=1
    for j in range(0,i):
        print("*",end="   ")
    print("\n")
