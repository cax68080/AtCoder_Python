from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
list_a = list(map(int,readline().rstrip("\n").split()))
list_a.sort(key=None,reverse=False)
result = 0
for i in range(n):
    if n > 0:
        if list_a[i - 1] + 1 != list_a[i]:
            result = list_a[i - 1] + 1
print(result)

        
