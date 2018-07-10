a=input()
count=0
if int(a)==1:
    print("No")
else :
    a=int(a)
    for i in range(2,a):
        if a%i==0:
            count=1
    if count==1:
        print("No")
    else:
        print("Yes")
