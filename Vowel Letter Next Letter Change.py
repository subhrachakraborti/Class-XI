st1 = input("Enter The String In UpperCase : ")
st2 = ""
for i in range(0,len(st1)):
    if st1[i] == 'A':
        st2 += 'B'
    elif st1[i] == 'E':
        st2 += 'F'
    elif st1[i] == 'I':
        st2 += 'J'
    elif st1[i] == 'O':
        st2 += 'P'
    elif st1[i] == 'U':
        st2 += 'V'
    else:
        st2 += st1[i]
print(st2)
