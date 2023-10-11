x=5
for i in range(0,5):
    for j in range(x,0,-1):
        print(" ",end=" ")
    x-=1
    for j in range(0,i):
        print("*",end="   ")
    print("\n")
