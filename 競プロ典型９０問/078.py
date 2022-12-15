from sys import stdin
readline = stdin.readline
n,m = map(int,readline().split())
list_result = [0 for i in range(n + 1)]
result = 0
for i in range(m):
    a,b = map(int,readline().split())
    if a > b:
        list_result[a] += 1
    else:
        list_result[b] += 1
print(list_result.count(1))
#print(list_result)