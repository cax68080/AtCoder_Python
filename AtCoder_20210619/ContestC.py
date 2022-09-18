from sys import stdin
import itertools
readline = stdin.readline
def fab():
    cnt = 0
    n = int(readline())
    a = list(map(int,readline().split()))
    b = list(itertools.combinations(a,2))
    for i in b:
        if i[0] != i[1]:
            cnt += 1
    return cnt
print(fab())

