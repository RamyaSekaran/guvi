a=input()
if a.isalpha():
	print("invalid")
else:
	a=int(a)
	for i in range(1,6):
		if(i==5):
			print(a*i)
		else:
		    print(a*i,end=' ')
