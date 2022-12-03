from sys import stdin
readline = stdin.readline
def fab(s,t):
    if s < t:
        result = "Yes"
    else:
        result = "No"
    return result
s,t = map(str,readline().split())
print(fab(s,t))
