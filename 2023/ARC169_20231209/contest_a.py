from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
a_list = [0]  + list(map(int,readline().rstrip("\n").split()))
p_list = [0,0] + list(map(int,readline().rstrip("\n").split()))
loop_cnt = 10 ** 100 + 2
p_index = 0
print(n)
print(a_list)
print(p_list)
for _ in range(2,loop_cnt):
    for i in range(n):
        p_index = abs(p_list[i])
        a_list[p_index] += a_list[i]
if a_list[0] == 0:
    print("0")
elif a_list[0] > 0:
    print("+")
elif a_list[0] < 0:
    print("-")
else:
    pass