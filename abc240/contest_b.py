from sys import stdin
readline = stdin.readline
n = int(readline())
a_list = list(map(int,readline().split()))
set_a = set()
for i in range(n):
    set_a.add(a_list[i])
print(len(set_a))