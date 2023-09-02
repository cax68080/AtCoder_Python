from sys import stdin
readline = stdin.readline
n,h,x = map(int,readline().rstrip("\n").split())
list_p = list(map(int,readline().rstrip("\n").split()))
#print(list_p)
min_p = 0
result = 0
for i in range(n):
    if h + list_p[i] >= x:
        if result == 0:
            result = i + 1
            min_p = list_p[i]
        elif min_p >=  list_p[i]:
            result = i + 1
            min_p = list_p[i]
        else:
            pass
print(result)

