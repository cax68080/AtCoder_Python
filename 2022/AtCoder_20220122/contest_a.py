from sys import stdin
readline =stdin.readline
n = int(readline())
list_a = list(map(int,readline().split()))
list_result = []
k = 0
for i in range(n - 1):
    if (i < n - 1) and (list_a[i] > list_a[i + 1]):
        k = list_a[i]
        break
if k == 0:
    k = list_a[n - 1]
list_result = [l for l in list_a if l != k]
#result = ""
#for i in list_result:
#    result = result + str(i) + " "
print(*list_result)