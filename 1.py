a = input("Enter a string:")
dup = a[0]
a = a.replace(dup,"$")
a = dup+a[1:]
print("String after replacing is:",a)