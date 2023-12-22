print("\t"," *")
for i in range(5,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(5,i-1,-1):
        if k<5 and k>0:
            print(" ",end=" ")
        else:
            print("*",end="   ")
    for l in range(6,i,-1):
        if l<7 and l>i+1:
            print(" ",end=" ")
        else:
            print("*",end="   ")
    print()
for i in range(4,0,-1):
    for l in range(5,i,-1):
        print(" ",end=" ")
    for m in range(1,i+1):
        if m>1 and m<i+1:
            print(" ",end=" ")
        else:
            print("*",end="   ")
    for n in range(1,i+1):
        if n>0 and n<m:
            print(" ",end=" ")
        else:
            print("*",end="   ")
    print()
print("\t"," *")
