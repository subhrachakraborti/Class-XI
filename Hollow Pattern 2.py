print(5*" ",8*"* ")
for i in range(2,0,-1):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range(0,8):
        if k>0 and k<7:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
print(8*"* ")
