from sys import stdin
readline = stdin.readline
n,m = map(int,readline().split())
s = ""
t = ""
list_s = []
list_t = []
count = 0
for _ in range(n):
    s = readline().rstrip('\n')
    list_s.append(s)
for _ in range(m):
    t = readline().rstrip('\n')
    list_t.append(t)
for i in list_s:
    if list_t.count(i[3:]) > 0:
        count += 1
print(count)

