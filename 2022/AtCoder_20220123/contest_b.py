from sys import stdin
from collections import defaultdict
readline = stdin.readline
def fab(n,a_list):
    for i in map(int,readline().split()):
        a_list[i] += 1
    #print(a_list)
    for i in range(1,n + 1):
        if a_list[i] == 3:
            result = i
            break
    return result 
n = int(readline())
#a_list = list(map(int,readline().split()))
a_list = defaultdict(int)
print(fab(n,a_list))
