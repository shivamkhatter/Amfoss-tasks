A= list(map(int,input().strip().split()))[:2]
a=A[0]
b=A[1]
z=b/a
y=0
flag=0
if b%a==0 and b>a:
    while z%2==0:
        z=z/2
        y+=1
    while z%3==0:
        z=z/3
        y+=1
    if z==1:
        print(y)
        flag=1
if b==a:
    print(0)
    flag=1
if flag==0:
    print(-1)
    
    