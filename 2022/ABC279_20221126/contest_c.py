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
list_a.sort(key=None,reverse=False)
list_b.sort(key=None,reverse=False)
result = "Yes"
for j in range(w):
    if list_a[j] != list_b[j]:
        result = "No"
        break
print(result)






