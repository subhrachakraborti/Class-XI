country = {"India":"New Delhi","Japan":"Tokyo","USA":"Washington D.C.","Russia":"Moscow","Ukraine":"Kiev"}
country2 = {"USA":"Washington","Russia":"Moscow","Ukraine":"Kiev", "Afghanistan":"Kabul"}
country.update(country2)
print(country)
l = len(country)
print("Length = ",l)
cntry = input("Enter Country Name: \n")
newCap = input("Enter The New Capital: \n")
country[cntry]=newCap
print("The changed data is",country[cntry])
