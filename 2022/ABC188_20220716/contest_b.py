from sys import stdin
readline = stdin.readline
n = int(readline())
a_list = list(map(int,readline().split()))
b_list = list(map(int,readline().split()))
result = 0
for i in range(n):
    result += a_list[i] * b_list[i]
if result == 0:
    print("Yes")
else:
    print("No")