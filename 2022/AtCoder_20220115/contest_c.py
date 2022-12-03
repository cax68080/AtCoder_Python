from sys import stdin
from collections import defaultdict
readline = stdin.readline
def fab(n,m,x,k):
    result = 0
    if k <= len(m[x]):
        result = m[x][k - 1]
    else:
        result = -1
    return result
n,q = map(int,readline().split())
a_list = list(map(int,readline().split()))
m = defaultdict(list)
for i in range(n):
    m[a_list[i]].append(i + 1)
for i in range(q):
    x,k = map(int,readline().split())
    print(fab(n,m,x,k))

