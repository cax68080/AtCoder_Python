from sys import stdin
readline = stdin.readline
a,b,k = map(int,readline().split())
list_a = []
num_a = 0
num_b = 0
for i in range(k):
    if i == 0:
        num_a = a
        num_b = b
    else:
        if num_a < b:
            num_a += 1
        if num_b > a:
            num_b -= 1
    if list_a.count(num_a) == 0:
        list_a.append(num_a)
    if list_a.count(num_b) == 0:
        list_a.append(num_b)
list_a.sort(key=None,reverse=False)
for i in list_a:
    print(i)

