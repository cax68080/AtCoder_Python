from sys import stdin
readline = stdin.readline
n,s,d = map(int,readline().split())
result = "No"
for _ in range(n):
    x,y = map(int,readline().split())
    if (x < s) and (y > d):
        result = "Yes"
        break
    else:
        pass
print(result)

