from sys import stdin
readline = stdin.readline
a0,k = map(int,readline().split())
def f(n):
    n_min = g1(n)
    n_max = g2(n)
    return n_max - n_min
def g1(x):
    list_x = list(str(x))
    list_x.sort(key=None,reverse=False)
    result = ""
    for i in list_x:
        result = result + i
    return int(result)
def g2(y):
    list_y = list(str(y))
    list_y.sort(key=None,reverse=True)
    result = ""
    for i in list_y:
        result = result + i
    return int(result)
ak = 0
for i in range(k + 1):
    if i == 0:
        ak = a0
    else:
        ak = f(ak)
print(ak)