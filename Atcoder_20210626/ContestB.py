from sys import stdin
readline=stdin.readline
def fab(s,t,u,v):
    i = 0
    x = 0
    cnt = 0
    while i == 0:
        if u*v - t == 0:
            cnt = -1
            break
        if s / (u*v - t) < 0.0:
            cnt = -1
            break
        if s <= x * v:
            break
        s = s + t
        x = x + u
        cnt += 1
    return cnt
a,b,c,d = map(int,readline().split())
print(fab(a,b,c,d))

