a,k=input().split()
a=int(a)
k=int(k)
for i in range(a,k):
    b=i
    c=0
    while b!=0:
        d=b%10
        c=c+(d*d*d)
        b=int(b/10)
    if(c==i):
        print(c)
