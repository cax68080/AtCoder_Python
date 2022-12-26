from sys import stdin
readline = stdin.readline
l,r = map(int,readline().split())
str_count = 0
for i in range(l,r + 1):
    str_count += len(str(i)) * i
print(str_count % (10 ** 9 + 7))