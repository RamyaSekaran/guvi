a=int(input())
b=a
c=0
while b!=0:
    d=b%10
    c=c+(d*d*d)
    b=int(b/10)
if c==a:
    print("yes")
else:
    print("no")
