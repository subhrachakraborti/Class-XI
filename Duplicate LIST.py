a = int(input("Enter number of values\n"))
print("Enter the values")
lst = []
for i in range(0,a):
    b = int(input())
    lst.append(b)
index = 0
while index < len(lst):
    value1 = lst[index]
    count = lst.count(value1)
    if count > 1:
        for i in range(count):
            lst.remove(vaue1)
        lst.append(value1)
    else:
        index += 1
print(lst)
