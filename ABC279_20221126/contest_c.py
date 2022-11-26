from sys import stdin
readline = stdin.readline
h,w = map(int,readline().split())
list_a = [[] for _ in range(w)]
list_b = [[] for _ in range(w)]
#print(list_a)
#print(list_b)
for _ in range(h):
    a = list(str(readline().rstrip('\n')))
    for i in range(w):
        list_a[i].append(a[i])
for _ in range(h):
    b = list(str(readline().rstrip('\n')))
    for i in range(w):
        list_b[i].append(b[i])
#print(list_a)
#print(list_b)
cnt = 0
for j in range(w):
    for k in range(w):
        if list_a[k] == list_b[j]:
            cnt += 1
            break
if cnt == w:
    print('Yes')
else:
    print('No')







