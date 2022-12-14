c=int(input())
x=1
for n in range(0,c):
    N=int(input())
    A= list(map(int,input().strip().split()))[:N]
    al=len(A)
    for i in range (al):
        flag=1
        if A[i]%A[0]!=0:
            flag=0
            break
    if flag==0:
        print("NO")
    else:
        print("YES")