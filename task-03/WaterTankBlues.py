c=int(input())
fl=[]
for n in range(0,c):
    N=int(input())
    A= list(map(int,input().strip().split()))[:N]
    al=len(A)
    A.pop(al-1)
    while len(A)>0 and A[0]==0:
        A.pop(0)
    al=len(A)
    for x in range(al):
        if A[x]==0:
            A[x]=1
    
    print(sum(A)+0 )