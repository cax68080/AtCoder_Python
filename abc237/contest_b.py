from sys import stdin
readline = stdin.readline
h,w = map(int,readline().split())
d = []
for i in range(h):
    list_d = list(map(str,readline().split()))
    d.append(list_d)
e = []
for j in range(w):
    for k in range(h):
        e.append(d[k][j])
    print(*e)
    e = []
