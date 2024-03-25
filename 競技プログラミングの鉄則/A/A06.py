from sys import stdin
readline = stdin.readline
n,q = map(int,readline().rstrip("\n").split())
list_a = list(map(int,readline().rstrip("\n").split()))
list_sum = []
a_sum = 0
for i in list_a:
    a_sum += i
    list_sum.append(a_sum)
#print(list_sum)
for _ in range(q):
    l,r = map(int,readline().rstrip("\n").split())
    if l - 2 < 0:
        print(list_sum[r - 1])
    else:    
        print(list_sum[r - 1] - list_sum[l - 2])
