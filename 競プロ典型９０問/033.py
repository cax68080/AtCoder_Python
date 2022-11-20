from sys import stdin
readline = stdin.readline
h,w = map(int,readline().split())
if (h == 1) or (w == 1):
    print(h * w)
else: 
    if h % 2 == 0:
        h = h // 2
    else:
        h = h //2 + 1
    if w % 2 == 0:
        w = w //2 
    else:
        w = w //2 + 1
    print(h * w)