from sys import stdin
readline=stdin.readline
def fab():
    n = int(readline())
    a = list(map(int,readline().split()))
    b = sorted(a,reverse=True)
    cnt = b[1]
    result = a.index(cnt) + 1
    return result
print(fab())