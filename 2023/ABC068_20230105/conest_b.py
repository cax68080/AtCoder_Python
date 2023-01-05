from sys import stdin
readline = stdin.readline
n = int(readline())
s = 0
r = 0
count_s = 0
result = 1
max_s = 0
for i in range(1,n + 1):
    s = i
    while True:
        r = s // 2
        if r > 0:
            count_s += 1
            s = r
        elif (r == 0) and (count_s > max_s):
            max_s = count_s
            result = i
            count_s = 0
            break
        else:
            count_s = 0
            break
print(result)

