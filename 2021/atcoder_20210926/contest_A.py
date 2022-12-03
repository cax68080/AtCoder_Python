from sys import stdin
readline = stdin.readline
def fab(a,b,c):
    cnt = 0
    baic = c
    result = 0
    if c == 0:
        return -1 
    else:
        while baic <= b:
            baic = c * cnt
            if a <= baic <= b:
                result = baic
                break
            else:
                cnt += 1
        if result == 0:
            return -1
        else:
            return result
a,b,c = map(int,readline().split())
print(fab(a,b,c))
