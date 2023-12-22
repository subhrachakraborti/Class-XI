l1 = eval(input("Enter words in a list : "))
l2 = []
d1 = d = {}
for el in l1:
    if el not in l2:
        l2.append(el)
for e in l2:
    c = l1.count(el)
    d = {e:c}
    d1.update(d)
    d = {}
print("Frequency : ",d1)
