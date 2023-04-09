import math
from sys import stdin
readline = stdin.readline
n = int(readline())
#n = int(math.sqrt(n))
num_set = set()
ans = 0
i = 1
while i ** 2 <= n:
    if n % i == 0:
        num_set.add(i)
        ans = n // i
        num_set.add(ans)
    else:
        pass
    i += 1
num_list = list(num_set)
num_list.sort(key=None,reverse=False)
for i in num_list:
    print(i)


