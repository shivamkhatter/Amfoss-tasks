c=int(input())
n=1
fl=[]
mana=int(0)
for n in range(0,c):
    N=int(input())
    A= list(map(int,input().strip().split()))[:N]
    A.sort()
    lenA=len(A)
    if lenA<N:
        H=N-lenA
        for l in range (1,H):
            A.append(0)
    A.sort()
    ele=int(0)
    for ele in range (0,lenA-1):
        e1=A[ele]
        e2=A[ele+1]
        if e1==0:
            g=int(0)
            for ele in range (0,lenA-1):
                eleO=A[ele]
                if eleO>0:
                    g=g+1
            mana=g+1
            break
        elif e1==e2:
            mana=lenA
            break
        else:
            mana=lenA+1
    fl.append(mana)
    n=n+1

for x in fl:
    print (x)