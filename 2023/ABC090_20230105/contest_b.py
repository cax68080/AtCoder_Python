from sys import stdin
readline = stdin.readline
a,b = map(int,readline().split())
list_num = []
count = 0
for i in range(a,b + 1):
    list_num = list(str(i))
    if (list_num[0] == list_num[4]) and (list_num[1] == list_num[3]):
        count += 1
    else:
        pass
print(count)