from sys import stdin
readline = stdin.readline
n,s,k = map(int,readline().rstrip("\n").split())
total = 0
for _ in range(n):
    p,q = map(int,readline().rstrip("\n").split())
    total += p * q
if total >= s:
    print(total)
else:
    print(total + k)
    