from sys import stdin
readline = stdin.readline
a,b,k = map(int,readline().split())
cnt = 0
s = a
while True:
    if s >= b:
        print(cnt)
        break
    else:
        s = s * k
        cnt += 1



