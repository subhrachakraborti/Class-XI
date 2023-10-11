list1 = eval(input("Enter the list"))
length = len(list1)
list2 = []
for i in range(length,0,-1):
    print(i)
list1.reverse()
list2 = list1
print(list2)
