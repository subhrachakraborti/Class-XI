print("1. Add a new contact\n2. Look up for a contact\n3. Exit")
o = n = phn = 1
nam = name = ""
d1 = {}
while o == 1:
    n = int(input("Enter your choice : "))
    if n == 1:
        nam = input("Enter Name : ")
        phn = int(input("Enter Phone No. : "))
        d = {nam:phn}
        d1.update(d)
        print("Contact added succesfully!\n")
    elif n == 2:
        name = input("Enter name to check : ")
        if name in d1:
            print("Phone number = ",d1[name])
        else:
            print("Not Found!\n")
    elif n == 3:
        break
    o = int(input("Enter 1 to continue : "))
