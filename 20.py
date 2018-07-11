a=input()
if a.isalpha():
	print("invalid")
else:
	a=int(a)
	for i in range(1,6):
		print(a*i)
