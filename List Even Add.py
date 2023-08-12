summ = 0
l = eval(input("Enter the elements:"))
for i in range(len(l)):
    if l[i] % 2 == 0:
        summ += l[i]
print("The sum of even elements is:", summ)
