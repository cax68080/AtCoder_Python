from sys import stdin
readline = stdin.readline
def fab(v,a,b,c):
    s = v % (a + b + c)
    #print(s)
    if s  < a:
        return "F"
    else:
        s = s - a
    if  s < b:
        return "M"
    else:
        s = s - b
    return "T"
v,a,b,c = map(int,readline().split())
print(fab(v,a,b,c))
