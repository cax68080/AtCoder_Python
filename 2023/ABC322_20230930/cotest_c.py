from sys import stdin
readline = stdin.readline
n,m = map(int,readline().rstrip("\n").split())
a = list(map(int,readline().rstrip("\n").split()))
day = 0
cnt = 0
for i in range(n):
    day = i + 1
    if a[cnt] > day:
        print(a[cnt] - day)
    elif a[cnt] == day:
        print(0)
        cnt += 1
    else:
        cnt += 1
    if cnt >= m:
        break