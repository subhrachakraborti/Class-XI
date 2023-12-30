from collections import Counter
l1 = eval(input("Enter your words in a list: "))
d1, d2 = {}, {}
for i in range(len(l1) - 1):
    el1 = l1[i]
    for el2 in l1[i + 1:]:
        l2 = list(el1)
        l3 = list(el2)
        for e in l2:
            c = l2.count(e)
            d1[e] = c
        for e in l3:
            c = l3.count(e)
            d2[e] = c
        if Counter(d1) == Counter(d2):
            print(el1, "is an anagram of", el2)
        d1, d2 = {}, {}
