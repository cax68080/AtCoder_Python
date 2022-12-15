from sys import stdin
import math
readline = stdin.readline
n = int(readline())
pos_list = []
for i in range(n):
    a = list(map(int,readline().split()))
    pos_list.append(a)
    pos_max = 0
for i in range(len(pos_list)):
    for j in range(i + 1,len(pos_list)):
        x = abs(pos_list[i][0] - pos_list[j][0])
        y = abs(pos_list[i][1] - pos_list[j][1])
        if pos_max < x ** 2 + y ** 2:
            pos_max = x ** 2 + y ** 2
result = math.sqrt(pos_max)
print(result)
