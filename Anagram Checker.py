from collections import Counter
l1 = eval(input("Enter your words in a list : "))
l2, l3 = [], []
d, d1, d2, dx = {}, {}, {}, {}
el, e = "", ""
for i in range(0, len(l1)-2):
    for j in range(i+1, len(l1)-1):
        el1, el2 = l1[i], l1[j]
        
        for el in list(el1):
            if el not in l2:
                l2.append(el)
                
        for e in l2:
            c = el1.count(e)
            d = {e: c}
            d1.update(d)
            d = {}
            
        for e in list(el2):
            if e not in l3:
                l3.append(el)
                
        for e in l3:
            c = el2.count(e)
            dx = {e: c}
            d2.update(dx)
            dx = {}
            
    if Counter(d1) == Counter(d2):
        print(el1,"is an anagram of",el2)
