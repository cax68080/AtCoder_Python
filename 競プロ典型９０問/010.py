from sys import stdin
readline = stdin.readline
n = int(readline())
point_1_list = [0] * n
point_2_list = [0] * n
num_class = 0
point = 0
result_1 = 0
result_2 = 0
for i in range(n):
    num_class,point = map(int,readline().split())
    if num_class == 1:
        result_1 += point
    else:
        result_2 += point
    point_1_list[i] = result_1
    point_2_list[i] = result_2 
#print(point_1_list)
#print(point_2_list)
q = int(readline())
point_1 = 0
point_2 = 0
for _ in  range(q):
    l,r = map(int,readline().split())
    if l - 2 < 0:
        l = -1
    else:
        l = l - 2
    if r - 1 <= 0:
        r = 0
    else:
        r = r -1
    if l == -1:
        point_1 = point_1_list[r]
        point_2 = point_2_list[r]
    else:
        point_1 = point_1_list[r] - point_1_list[l]
        point_2 = point_2_list[r] - point_2_list[l]
    print(point_1," ",point_2)
        