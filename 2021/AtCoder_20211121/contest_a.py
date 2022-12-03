from sys import stdin
readline = stdin.readline
def fab(n,l,r):
    cnt = 0
    x = 0
    for i in range(l,r+1):
        x = i
        ans = x ^ n
        if ans < n:
            cnt += 1
    return cnt
n,l,r = map(int,readline().split())
print(fab(n,l,r))
