from sys import stdin
readline = stdin.readline
n = int(readline())
t = 0
a_list = []
b_list = []
for i in range(n):
    a,b = map(int,readline().split())
    a_list.append(a)
    b_list.append(b)
    t += round(a/b,5)
t2 = round(t/2,5)
for j in range(n):
    s = round(a_list[j]/b_list[j],5)

