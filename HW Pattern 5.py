a = 1
for i in range(1,5):
    x = a+i-1
    for j in range(i,0,-1):
        print(x,end=" ")
        x-=1
    print()
    a+=i
