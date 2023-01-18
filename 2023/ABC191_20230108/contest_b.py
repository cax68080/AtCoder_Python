from sys import stdin
readline = stdin.readline
n,x = map(int,readline().split())
a_list = list(map(int,readline().split()))
result_list = []
for i in range(n):
    if a_list[i] == x:
        pass
    else:
        result_list.append(a_list[i])

print(*result_list)

