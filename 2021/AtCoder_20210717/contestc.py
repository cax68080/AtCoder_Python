from sys import stdin
import cProfile
readline=stdin.readline
def fab():
    n,k = map(int,readline().split())
    c = list(map(int,readline().split()))
    bg = 0
    bg0 = 0
    for i in range(n):
        if i+k > len(c):
            break
        else:
            l = c[i:i+k]
            l = set(l)
            bg = len(l)
            if bg0 < bg:
                bg0 = bg
    return bg0
print(fab())
#cProfile.run(fab())
