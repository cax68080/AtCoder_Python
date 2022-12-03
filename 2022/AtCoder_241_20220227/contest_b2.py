from collections import Counter
from sys import stdin
readline = stdin.readline
n,m = map(int,readline().split())
a_list = Counter(readline().split())
b_list = Counter(readline().split())
if len(b_list - a_list) != 0:
    print("No")
else:
    print("Yes")
