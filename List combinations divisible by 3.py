list1 = list(map(int, input("Enter five numbers: ").split()))
count = 0
for i in range(0,5):
    s = 0
    if i%3 == 0:
        
    for j in range(4,i,-1):
        s += list1[j]
    if s%3 == 0:
        count += 1
print(count)
