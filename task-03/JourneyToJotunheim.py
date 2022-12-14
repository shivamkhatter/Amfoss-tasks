x = int(input(""))
for y in range(x):
    n = int(input(""))
    ai = list(map(int, input("").split()))
    flag = 0
    while n > 0:
        n = ai[n - 1]
        flag += 1
    if flag != 3:
        print("NO")
    else:
        print("YES")