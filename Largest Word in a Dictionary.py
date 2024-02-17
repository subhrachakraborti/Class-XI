d = eval(input("Enter your dictionary : "))
long = ''
for key in d:
    if len(key) > len(long):
        long = key
print("The longest key is:", long)
