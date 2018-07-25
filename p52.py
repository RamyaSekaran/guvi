a=[]
b=[]
count=0
for i in range(4):
    x,y=(input().split())
    a.append(x)
    b.append(y)
for i in range(4):
	for j in range(i+1,4):
		if a[i]==a[j]:
			a[i]=0
			a[j]=0
		if b[i]==b[j]:
			b[i]=0
			b[j]=0
for i in range(4):
	if a[i]!=0:
		count=1
	if b[i]!=0:
		count=1
if count==0:
	print("yes")
else:
	print("no")
