from sys import stdin
readline = stdin.readline
n = int(readline())
list_s = list(map(int,readline().split()))
s_item = 0
a_total = 0
a_list = []
for i in (list_s):
    s_item = i - a_total
    a_list.append(s_item)
    a_total += s_item
    s_item = 0
print(*a_list)