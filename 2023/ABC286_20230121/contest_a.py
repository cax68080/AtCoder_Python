from sys import stdin
readline = stdin.readline
n,p,q,r,s = map(int,readline().split())
list_a = list(map(int,readline().split()))
list_result = []
for i in range(len(list_a)):
    if i < (p - 1):
        list_result.append(list_a[i])
    elif (p - 1) <= i <= (q - 1):
        list_result.append(list_a[i + (r - p)])
    elif (r - 1) <= i <= (s - 1):
        list_result.append(list_a[i - (r - p)])
    else:
        list_result.append(list_a[i])
print(*list_result)

