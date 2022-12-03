from sys import stdin
readline = stdin.readline
def fab(n,s):
    n = n - 1
    if s[n] == "o":
        result = "Yes"
    else:
        result = "No"
    return result
n = int(readline())
s = str(readline())
print(fab(n,s))

