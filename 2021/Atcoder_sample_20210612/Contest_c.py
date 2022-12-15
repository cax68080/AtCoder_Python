from sys import stdin
readline = stdin.readline
def fab():
    l = list(map(int,readline().split()))
    l.sort(key=None,reverse=True)
    return(l[2])
print(fab())
