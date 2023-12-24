from sys import stdin
readline = stdin.readline
n,a,b = map(int,readline().rstrip("\n").split())
c_list = list(map(int,readline().rstrip("\n").split()))
print(c_list.index(a+b) + 1)