print("1. Add item to inventory\n2. Update item quantity\n3. Display inventory\n4. Calculate total value\n5. Quit")
inventory = d = {}
price = 0
o = 1
while o == 1:
    n = int(input("Enter your choice : "))
    if n == 1:
        d = eval(input("Enter inventory as : {inventory:[quantity,price per unit]} "))
        inventory.update(d)
    elif n == 2:
        index = input("Enter item name to update : ")
        if index in inventory:
            new_q = int(input("Enter new quantity : "))
            inventory[index][0] = new_q
    elif n == 3:
        print(inventory)
    elif n == 4:
        for item, details in inventory.items():
            price = price + details[1] * details[0]
        print("Total amount ?= ", price)
    elif n == 5:
        break
    o = int(input("Enter 1 to continue : "))
