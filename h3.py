n=int(input())
count=0
a=[int(i) for i in input().split()]
b=[]
for i in range(0,n):
    if i==a[i]:
        b.append(a[i])
        count=1
if count==1:
    for i in range (len(b)):
        if i==len(b)-1:
        	print(b[i])
        else:
        	print(b[i],end=" ")
else:
    print(-1)

		
