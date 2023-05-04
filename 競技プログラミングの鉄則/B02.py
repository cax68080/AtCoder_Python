from sys import stdin
readline = stdin.readline
a,b = map(int,readline().split())
result = "No"
for i in range(a,b + 1):
    if 100 % i == 0:
        result = "Yes"
        break
print(result)
