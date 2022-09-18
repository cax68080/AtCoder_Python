from sys import stdin
readline = stdin.readline
def fab(l,r,s):
    str_r = ""
    s = s.rstrip("\n")
    for i in range(r-1,l-2,-1):
        str_r = str_r + s[i]
    result = s[0:l-1] + str_r + s[r:]
    return result
l,r = map(int,readline().split())
s = str(readline())
print(fab(l,r,s))
