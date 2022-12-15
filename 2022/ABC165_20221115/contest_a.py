from sys import stdin
readline = stdin.readline
k = int(readline())
a,b = map(int,readline().split())
result = "NG"
for i in range(a,b + 1):
    if i % k == 0:
        result = "OK"
        break
print(result)