d = eval(input("Enter your dictionary : "))
n = int(input("Enter your number : "))
for key in d:
    d[key] = d[key]*n
print(d)
