from sys import stdin
readline = stdin.readline
n,k = map(int,readline().split())
a_list = list(map(int,readline().split()))
for _ in range(k):
    del a_list[0]
    a_list.append(0)
print(*a_list)