n = int(input())
a = list(map(int,input().split()))
a.sort(key=None,reverse=True)
j = 0
k = 0
t = 1
for i in range(n):
    if t % 2 != 0:
        j += a[i]
    else:
        k += a[i]
    t += 1
print(j - k)

