from sys import stdin
readline = stdin.readline
n = int(readline())
t,a = map(int,readline().split())
list_h = list(map(int,readline().split()))
min_tmp = 0
min_no = 0
for i in range(n):
    tmp = abs(a - (t - list_h[i] * 0.006))
    if i == 0:
        min_tmp = tmp
        min_no = i + 1
    elif (i > 0) and (min_tmp > tmp):
        min_tmp = tmp
        min_no = i + 1
    else:
        pass
print(min_no)