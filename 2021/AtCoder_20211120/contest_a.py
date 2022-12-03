from sys import stdin
readline = stdin.readline
def fab(s,t,x):
    if s < t:
        if s <= x < t:
            result = "Yes"
        else:
            result = "No"
    else:
        if s <= x or x < t:
            result = "Yes"
        else:
            result = "No"
    return result
s,t,x = map(int,readline().split())
print(fab(s,t,x))