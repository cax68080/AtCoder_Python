from sys import stdin
from itertools import combinations as cm
readline = stdin.readline
n = int(readline())
a_list = list(map(int,readline().split()))
cnt = 0
for x in cm(a_list,3):
    #print(x)
    if len(set(x)) == 3:
        cnt += 1
print(cnt)

