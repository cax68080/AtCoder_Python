from sys import stdin
readline = stdin.readline
n,m = map(int,readline().rstrip("\n").split())
s_list = list(str(readline().rstrip("\n")))
#print(s_list)
shirt_1 = 0
shirt_2 = 0
shirt_t = 0
max_1 = 0
max_2 = 0
max_t = 0
for i in range(n):
    if s_list[i] == "1":
        shirt_1 += 1
        shirt_t += 1
    elif s_list[i] == "2":
        shirt_2 += 1
        shirt_t += 1
    else:
        if max_t < shirt_t:
            max_t = shirt_t
        if max_2 < shirt_2:
            max_2 = shirt_2
        shirt_1 = 0
        shirt_2 = 0
        shirt_t = 0
if max_t < shirt_t:
    max_t = shirt_t
if max_2 < shirt_2:
    max_2 = shirt_2

print(max(max_2,max_t - m))