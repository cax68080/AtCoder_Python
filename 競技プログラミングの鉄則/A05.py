from sys import stdin
readline = stdin.readline
n,k = map(int,readline().split())
cnt = 0
for i in range(1,n + 1):
    for j in range(1,n + 1):
        #print(i,j)
        if i + j >= k:
            break
        else:
            pass
        if k - (i + j) <= n:
            cnt += 1
        else:
            pass
    if i >= k:
        break
    else:
        pass
print(cnt)
