from sys import stdin
readline=stdin.readline
def fab(x,y):
    result = ""
    if 6 * x >= y:
        result = "Yes"
    else:
        result = "No"
    if x > y:
        result = "No"
    return result
a,b = map(int,readline().split())
print(fab(a,b))
