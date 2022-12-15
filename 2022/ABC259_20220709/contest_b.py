import math
from sys import stdin
readline = stdin.readline
a,b,d = map(int,readline().split())
r = math.sqrt(a ** 2 + b ** 2)
t = math.atan2(b,a)
t = 180 / math.pi * t
t = t - d
an = math.cos(t) * r
bn = math.sin(t) * r
print(r)
print(an)
print(bn)
print(t)
