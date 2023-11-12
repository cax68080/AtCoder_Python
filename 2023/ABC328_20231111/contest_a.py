from sys import stdin
readline = stdin.readline
n,x = map(int,readline().rstrip("\n").split())
s_list = list(map(int,readline().rstrip("\n").split()))
total = 0
for i in s_list:
    if i <= x:
        total += i
print(total)
