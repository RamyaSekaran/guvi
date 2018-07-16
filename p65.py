n,k=input().split()
n=int(n)
k=int(k)
a=[int(i) for i in input().split()]
b=int(input())
sum=0
for i in range(0,n):
	sum=sum+a[i]
if sum/2==b:
	print(int(a[k]/2))
else:
	print("Bon Appetit")
