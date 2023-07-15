print("List Of Prime Numbers")
for i in range (2, 100):
    count = 0
    a = 1
    while(a < i):
        if(i%a == 0):
            count = count + 1
        a = a + 1
    if(count == 1):
        print(i)
