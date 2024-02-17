d1 = eval(input("Enter your dictionary : "))
l1 = d1.values()
l2 = list()
for i in l1:
    if i not in l2:
        l2.append(i)
print("Unique values = ",l2)
