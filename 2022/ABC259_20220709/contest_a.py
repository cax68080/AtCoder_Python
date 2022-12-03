from sys import stdin
readline = stdin.readline
n,m,x,t,d = map(int,readline().split())
z = t - d * x
if m >= x:
    print(t)
else:
    print(z + (d * m)) 
