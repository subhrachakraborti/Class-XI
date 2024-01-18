months = {"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
user = input("Enter month : ")
print(user,months[user],sep="\t")
k = months.keys()
v = months.values()
l1 = []
print("The months are",k,sep=" ")
for keys in months:
    if months[keys] == 31:
        l1.append(keys)
print("The months with 31 days : ",l1)
sk = sorted(k)
nm = {}
for i in sk:
    nm[i] = months[i]
print("Sorted dictionary : ",nm)
