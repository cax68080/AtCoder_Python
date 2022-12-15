from sys import stdin
readline = stdin.readline
def fab(n,s):
    mx = s
    mn = s
    x = s.rstrip('\n')
    for i in range(n):
        x = x[1:] + x[0]
        if mx < x:
            mx = x
        if mn > x:
            mn = x
    return mn,mx
s = str(readline())
n = len(s)
mn,mx = map(str,fab(n,s))
print(mn)
print(mx)
