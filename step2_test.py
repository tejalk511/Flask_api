import step1_making

print("Enter values of parameters : ")
a = float(input("Enter TLC value: \n"))
#b = float(input("Enter Lymphocytes value: \n"))
#c = float(input("Enter Polymorphs value: \n"))
#d = float(input("Enter Monocytes value: \n"))
#e = float(input("Enter Eosinophiles value: \n"))
f = float(input("Enter Protein value: \n"))
g = float(input("Enter Sugar value: \n"))

print(" ****************************** ")
print("**** Results are : ********* ")
result = step1_making.model.predict([[a,f,g]])
print(result)
print("\n")
print("\n")
print(" ****************************** ")
print("\n")
print("\n")