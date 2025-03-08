from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n")) * 2
a_list = list(map(int,readline().rstrip("\n").split()))
a_list_odd = []
a_list_even = []
count = 0
old = 0
for i in range(len(a_list)):
    if i % 2 == 0:
        a_list_even.append(a_list[i])
    else:
        a_list_odd.append(a_list[i])
for i in a_list_odd:
    if old == i:
        count += 1
    old = i
old = 0
for i in a_list_even:
    if old == i:
        count += 1
    old = i
print(count)

