d1 = eval(input("Enter your dictionary : "))
l1 = sorted(d1.values())
d2 = dict()
for i in l1:
    for j in d1:
        if i == d1[j]:
            d2[j] = i
print(d2)
