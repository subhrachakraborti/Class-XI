st = input("Enter The String : ")
length = len(st)
if length < 3 :
    print("Your String is",st)
elif length >= 3 :
    if "ing" in st :
        print("Your String is ",st,"ly.",sep="")
    else :
        print("Your String is ",st,"ing.",sep="")
