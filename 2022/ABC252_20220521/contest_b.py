from sys import stdin
readline = stdin.readline
n,k = map(int,readline().split())
list_a = list(map(int,readline().split()))
list_b = list(map(int,readline().split()))
max_a = max(list_a)
result = 'No'
for i in list_b:
    ix = i - 1
    if list_a[ix] == max_a:
        result = 'Yes'
        break
print(result)