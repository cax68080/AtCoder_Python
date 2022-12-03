from sys import stdin
readline = stdin.readline
def fab(n):
    a = 0
    b = 0
    c = 0
    r = 0
    cnt = 0
    while a <= n:
        a += 1
        if b >= a:
            continue
        else:
            b += 1
        if c >= b:
            r = a * b * c 
            while c >= b:
                c += 1
                r = a * b * c
                print(r)
                if n >= r:
                    cnt += 1
    return cnt

n = int(readline())
print(fab(n))