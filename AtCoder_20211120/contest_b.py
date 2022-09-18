from sys import stdin
from itertools import count
readline = stdin.readline
def fab(n,x,list_a):
    list_result = [0 for i in range(n+1)]
    list_result[x] = 1
    for i in count():
        j = list_a[x]
        if list_result[j] == 0:
            list_result[j] = 1
            x = j
        else:
            break
    result = list_result.count(1)
    return result
n,x = map(int,readline().split())
list_a = [0]
list_i = list(map(int,readline().split()))
list_a = list_a + list_i
print(fab(n,x,list_a))
