a=int(input("Enter the number"))
sum=0
b=a
while(a>0):
    d=a%10
    sum=(sum*10)+d
    a=a//10
if(sum==b):
    print("is a palindrome")
else:
    print("is not a palindrome")
