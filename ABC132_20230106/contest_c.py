from sys import stdin
readline = stdin.readline
n = int(readline())
d_list = list(map(int,readline().split()))
d_sort_list = sorted(d_list)
#print(d_list)
#print(d_sort_list)
pos = n // 2
pos_s = d_sort_list[pos - 1]
pos_e = d_sort_list[pos]
print(pos_e - pos_s)
