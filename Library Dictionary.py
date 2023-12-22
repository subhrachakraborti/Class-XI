library = d = {}
o = 1
while o==1:
    print("Enter 1 to add new books.")
    print("Enter 2 to search a book.")
    print("Enter 3 to print all books.")
    n = int(input("Enter : "))
    if n == 1:
        d = eval(input("Enter in sequence : {book:[author,year]} "))
        library.update(d)
    elif n == 2:
        sb = input("Enter the book name to search : ")
        if sb in library:
            print("It is already present.")
        else:
            print("It is not present.")
    elif n == 3:
        print(library)
    o = int(input("Enter 1 to continue : "))
