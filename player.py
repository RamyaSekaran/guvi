a=int(input())
c=0
temp=a
while(temp!=0):
    b=temp%10
    c=(c*10)+b
    temp=temp/10
print(c)
