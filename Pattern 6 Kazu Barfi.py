#n = int(input("Enter The Size of Kaju Barfi : "))
n = 5
x = n
for i in range(0,n+1):
    for j in range(x,0,-1):
        print(" ",end=" ")
    x-=1
    for j in range(0,i):
        print("*",end="   ")
    print("\n")
x = 1
for i in range(n-1,0,-1):
    for j in range(0,x):
        print(" ",end=" ")
    x+=1
    for j in range(0,i):
        print("*",end="   ")
    print("\n")
