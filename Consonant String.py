st1 = input("Enter The String In UpperCase : ")
st2 = ""
for i in range(0,len(st1)):
    if st1[i] == 'A' or st1[i] == 'E' or st1[i] == 'I' or st1[i] == 'O' or st1[i] == 'U':
        continue
    else:
        st2+=st1[i]
print(st2)
