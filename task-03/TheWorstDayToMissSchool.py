n=int(input())
a = list(map(int,input().strip().split()))[:n]
for x in range (0,n):
    if a[x]==0:
        a.pop(x)
a.sort()
al=len(a)
if al>3:
    for y in range (0,al-3):
        
        a1=a[y]+a[y+1]+a[y+2]+a[y+3]
        if a1==4:
            a.pop(y)
            a.pop(y+1)
            a.pop(y+2)    
            a.pop(y+3)
            a.append(a1)
    a.sort()
    al=len(a)
if al>2:
    for y in range (0,al-3):
        a1=a[y]+a[y+1]+a[y+2]
        if a1<=4:
            a.pop(y)
            a.pop(y+1)
            a.pop(y+2)
            a.append(a1)
    a.sort()
    al=len(a)
if al>1:
    for y in range (0,al-2):
        a1=a[y]+a[y+1]
        if a1<=4:
            a.pop(y)
            a.pop(y+1)
            a.append(a1)
    a.sort()
    al=len(a)

    
al=len(a)
print(al)