st1 = input("Enter The Number : ")
st2 = ""
for i in range(len(st1)-1,-1,-1):
    st2 += st1[i]
if st2 == st1:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
