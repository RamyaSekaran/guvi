a=input()
b=input()
count=0
if a.isalpha() or b.isalpha():
    print("invalid")
else:
    a=int(a)
    b=int(b)
    for i in range((a+1),b):
        for x in range(2,i):
            if i%x==0:
        	    count=1
        if count==0:
            print(i,end=' ')
        count=0
