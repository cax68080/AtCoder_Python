from sys import stdin
readline = stdin.readline
n,a = map(int,readline().rstrip("\n").split())
list_t = list(map(int,readline().rstrip("\n").split()))
result = 0
for i in list_t:
    if result >= i:
        result += a
        print(result)
    else:
        result = (i + a)
        print(result)
