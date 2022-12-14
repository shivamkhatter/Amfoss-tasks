x=input("")
count =0
while int(int(x)/10) != 0:
    n = 0
    for y in x:
        n += int(y)
    count += 1
    x = str(n)
print(count)