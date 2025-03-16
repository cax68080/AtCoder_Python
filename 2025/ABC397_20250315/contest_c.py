from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
a = list(map(int, readline().rstrip("\n").split()))
max_sum = 0
for i in range(n):
    l = len(set(a[0:i+1]))
    r = len(set(a[i+1:]))
    if max_sum < l+r:
        max_sum = l+r
print(max_sum)



