from sys import stdin
readline = stdin.readline
def POW(s,t,u):
    if u % 2 == 0:
        if abs(s) == abs(t):
            return "="
        elif abs(s) > abs(t):
            return ">"
        else:
            return "<"
    else:
        if s == t:
            return "="
        elif s > t:
            return ">"
        else:
            return "<"
a,b,c = map(int,readline().split())
x = POW(a,b,c)
print(x)
    