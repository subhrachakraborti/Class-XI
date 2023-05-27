n = int(input("Enter Your Number"))
m = n
Sum =0
while(n>0):
    a = n%10
    fact = 1
    for i in range(1, a+1):
        fact = fact * i
    Sum = Sum + fact
    n = n//10
if(Sum == m):
    print("Krishnamurthy No.")
else:
     print("Not a Krishnamurthy No.")
