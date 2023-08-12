summ = 0
count = 0
for i in range(4, 101):
    for j in range(4, 101, 2):
        if i % j == 0:
            count += 1
            summ += i
            break
avg = summ / count
print("The average is:", avg)
