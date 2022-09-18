from sys import stdin
readline = stdin.readline
def fab(n):
    s = 4 - len(n)
    result = "0" * s + n
    return result
n = str(readline()).rstrip('\n')
print(fab(n))
