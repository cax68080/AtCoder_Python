from sys import stdin
readline = stdin.readline
h,w = map(int,readline().split())
list_s = []
count = 0
for _ in range(h):
    list_s = list(readline().rstrip('\n'))
    count += list_s.count('#')
print(count)

