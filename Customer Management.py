#Customer Management
o = 1
customers = {}
lst = []
x = 0
while o == 1:
    choice = int(input("Enter 1 to add new user or 2 to check other: "))
    if choice == 1:
        n = int(input("How many new users? "))
        for i in range(0,n):
            name = input("Enter Name        : ")
            email = input("Enter Email      : ")
            phone_number = int(input("Enter Phone No.   : "))
            total_purchase = float(input("Enter Total Purchase: ₹"))
            print("Customer Added Successfully!")
            lst.append({email:[name, phone_number, total_purchase]})
            x += 1
    elif choice == 2:
        check = input("Enter an email to check: ")
        for i in range(len(lst)):
            if check in lst[i]:
                print(lst[i][email])
                break
        else:
            print("Not Found")
    o = int(input("Enter 1 to continue: "))
print("Thank You!\nSigning Off!!\nVisit again.")
