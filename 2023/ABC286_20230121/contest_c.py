from sys import stdin
readline = stdin.readline
n,a,b = map(int,readline().split())
count = n // 2
s = readline().rstrip("\n")
s_list = list(s)
r_list = s_list[:]
r_list.reverse()
total_a = 0
total_b = 0
min_total = 0
for i in range(count):
    if i > 0:
        t = s_list.pop(0)
        s_list.append(t)
        r_list = s_list[:]
        r_list.reverse()
        total_a += a
    #print(s_list)
    #print(r_list)
    for j in range(count):
        if s_list[j] == r_list[j]:
            pass
        else:
            total_b += b
    if min_total == 0 and total_a + total_b == 0:
        break
    elif min_total == 0:
        min_total = total_a + total_b
    elif min_total > (total_a + total_b):
        min_total = total_a + total_b
    else:
        pass
    total_b = 0
print(min_total)


