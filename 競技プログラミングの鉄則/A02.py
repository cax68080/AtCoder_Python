from sys import stdin
readline = stdin.readline
n,x = map(int,readline().split())
a_list = list(map(int,readline().split()))
if a_list.count(x) > 0:
    print("Yes")
else:
    print("No")
