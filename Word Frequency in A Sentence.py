st = input("Enter your sentence : ")
s = st.split()
l1 = list(s)
l2 = []
d1, d = {},{}
for el in l1:
    if el not in l2:
        l2.append(el)
for e in l2:
    c = l1.count(e)
    d = {e:c}
    d1.update(d)
    d = {}
print("Frequency : ",d1)
