n1=float(input("enter first no.:"))
n2=float(input("enter second no.:"))
n3=float(input("enter third no.:"))
if(n1>n2) and (n1>n3):
    largest=n1
elif (n2>n1)and (n2>n3):
    largest=n2
else:
    largest=n3
print("The largest number is:",largest)