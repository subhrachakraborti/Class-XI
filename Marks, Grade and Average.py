d1 = eval(input("Enter your dictionary : "))
l1 = d1.values()
avg = sum(l1)/len(l1)
print("The average grade = ",avg)
k = ''
c = 0
for key in d1:
    if d1[key] > c:
        c = d1[key]
        k = key
print("The highest grade is",k,"of",c)
