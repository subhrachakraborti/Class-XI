import random as r
n = int(input("Enter the length of your password : "))
h = n//2
s1 = str(r.randint(10000,h*10000))
s2 = h*(chr(r.randint(65,91)))
s3 = chr(r.randint(35,48))
s = list(s1+s2+s3)
r.shuffle(s)
st = ''.join(s)
print(st)
