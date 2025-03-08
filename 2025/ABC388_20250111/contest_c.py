from sys import stdin
from bisect import bisect_left
readline = stdin.readline
n = int(readline().rstrip("\n"))
list_a = list(map(int,readline().rstrip("\n").split()))
list_a.sort(key=None,reverse=False)
count = 0
for i in range(len(list_a)):
    target = list_a[i] * 2
    j = bisect_left(list_a, target, i + 1)
    count += len(list_a) - j

#for i in range(len(list_a)):
#    for j in range(i + 1,len(list_a)):
#       # print(list_a[i],list_a[j])
#        if list_a[i] * 2 <= list_a[j]:
#            count += 1 
#        #print(count)
print(count)