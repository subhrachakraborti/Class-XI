count = 0
Sum = 0
for i in range(1,101):
    even = False
    odd = False
    for j in range(2,i+1):
        if i%j == 0:
            if j%2 == 0:
                even = True
            else:
                odd = True
        if even and odd:
            count+=1
            Sum += i
            print(i)
avg = Sum/count
print(avg)
