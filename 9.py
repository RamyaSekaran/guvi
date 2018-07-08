N=input()
K=input()
sum=0
if N.isalpha() or K.isalpha():
    print("invalid")
else:
    N=int(N)
    K=int(K)
    arr=[int(input()) for _ in range(N)]
    for i in range(K):
        sum=sum+arr[i]
    print(sum)
