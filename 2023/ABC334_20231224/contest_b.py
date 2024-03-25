from sys import stdin
readline = stdin.readline
a,m,l,r = map(int,readline().rstrip("\n").split())
count = 0
pos = a
if a < l:
    while True:
        pos += m
        if (l <= pos) and (pos <= r):
            count += 1
        elif r < pos:
            break
    print(count)
if (a >= l) and (a <= r):
    while True:
        pos += m
        if (l <= pos) and (pos <= r):
            count += 1
        elif r < pos:
            break
    while True:
        pos -= m
        if (l <= pos) and (pos <= r):
            count += 1
        elif l > pos:
            break
    print(count)
if pos > r:
    while True:
        pos -= m
        if (l <= pos) and (pos <= r):
            count += 1
        elif l > pos:
            break
    print(count)

    
