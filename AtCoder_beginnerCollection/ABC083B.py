n,a,b = map(int,input().split())
total = 0
n += 1
for i in range(1,n):
    l = len(str(i))
    k = list(str(i))
    t = 0
    for j in range(l):
        t += int(k[j])
    if t >= a:
        if t <= b:
            total += i
print(total)
