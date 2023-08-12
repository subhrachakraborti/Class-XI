n  = int(input("Enter the range"))
a = 0
b = 1
c = 0
print(a)
print(b)
while(c<n):
    c = a+b
    a = b
    b = c
    print(c)
