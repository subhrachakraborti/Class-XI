lst = []
a = 0
for i in range(2,30):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2 :
        lst.append(i)
for m in range(1,len(lst)+1):
    for n in range(1,m+1):
        if a<len(lst):
            print(lst[a],end=" ")
            a+=1
    print()
