d1 = eval(input("Enter your dictionary : "))
for keys in d1:
    k = d1.values()
    if k.count(d1[keys]) == 2:
        print("2 keys have same values.")
    else:
        print("No keys have same values.")
