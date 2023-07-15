n = int(input("Enter 1 or 2 for Multipication or Divison"))
if(n == 1):
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    pro = 0
    while(a > 0):
        pro += b
        a -= 1
    print(pro)
elif(n == 2):
    c = int(input("Enter Dividend"))
    d = int(input("Enter Divisor"))
    count = 0
    while(c >= d):
        c -= d
        count += 1
    print("Quotient = ",count," Remainder = ",c)
