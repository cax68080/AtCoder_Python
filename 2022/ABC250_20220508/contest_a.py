from sys import stdin
readline = stdin.readline
h,w = map(int,readline().split())
r,c = map(int,readline().split())
if h == 1 and w == 1:
    result = 0
elif h == 1:
    if c == 1 or c == w:
        result = 1
    else:
        result = 2
elif w == 1:
    if r == 1 or r == h:
        result = 1
    else:
        result = 2
else:
    if r == 1 and c == 1:
        result = 2
    elif r == 1 and c == w:
        result = 2
    elif r == h and c == 1:
        result = 2
    elif r == h and c == w:
        result = 2
    elif r == 1 or r == h:
        result = 3
    elif c == 1 or c == w:
        result = 3
    else:
        result = 4
print(result)

