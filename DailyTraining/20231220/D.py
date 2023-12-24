from sys import stdin
readline = stdin.readline
n,m,t = map(int,readline().rstrip("\n").split())
a_list = list(map(int,readline().rstrip("\n").split()))
#print(a_list)
for i in range(m):
    x,y = map(int,readline().rstrip("\n").split())
    a_list[x - 1] = a_list[x - 1] - y
#print(a_list)
result = "Yes"
for i in a_list:
    if t - i > 0:
        t = t - i
    else:
        result = "No"
        break
print(result)
        