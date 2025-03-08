from sys import stdin
readline = stdin.readline
n,k = map(int,readline().rstrip("\n").split())
a_list = list(map(int,readline().rstrip("\n").split()))
count = 0
guest = 0
for i in a_list:
    if k >= guest + i:
        guest += i
    else:
        count += 1
        guest = 0
        guest += i
if guest > 0:
    count += 1
print(count)
