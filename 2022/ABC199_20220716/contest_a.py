from sys import stdin
readline = stdin.readline
a,b,c = map(int,readline().split())
if a ** 2 + b ** 2 < c ** 2:
    print("Yes")
else:
    print("No")