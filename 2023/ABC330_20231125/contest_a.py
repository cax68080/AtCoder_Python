from sys import stdin
readline = stdin.readline
n,l = map(int,readline().rstrip("\n").split())
a_list = list(map(int,readline().rstrip("\n").split()))
counter = 0
for i in a_list:
    if i >= l:
        counter += 1
print(counter)
