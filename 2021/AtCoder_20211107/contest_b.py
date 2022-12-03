from sys import stdin
readline = stdin.readline
n = int(readline())
l_list = set(readline() for i in range(n))
print(len(l_list))