n = int(input())
a = list(map(int,input().split()))
cnt = 0
b = []
for i in range(n):
    k = int(a[i] % 200)
    b.append(k)
for i in range(n):
    for j in range(i+1 ,n):
        if b[i] == b[j]:
            cnt += 1
print(cnt)

