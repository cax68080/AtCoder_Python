from sys import stdin
readlne = stdin.readline
def fab(s,t):
    x = 0
    x = s * t / 100
    return(x)
a,b = map(int,readlne().split())
print(fab(a,b))
