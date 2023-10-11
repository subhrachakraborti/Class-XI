code = input("Enter the code")
dcode = ""
code = "32"+code
for i in code:
    if (i>="65" and i<="90") or (i>="97" and i<="122") or i=="32" :
        #i = 
        if (i>="65" and i<="90"):
            dcode = dcode + chr(i)
        elif (i>="97" and i<="122"):
            dcode =dcode + chr(97)
        elif (i == "32"):
            dcode = dcode + " "
        else :
            continue
print(dcode)
