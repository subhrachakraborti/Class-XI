add = 0
div = 0
fact = 1
n = int(input("Enter the value of n \n"))
for i in range(1,n+1):
    fact = 1
    div = 0
    for j in range(1,i+1):
        fact *= j
    div = 1/fact
    add += div
print(add)
