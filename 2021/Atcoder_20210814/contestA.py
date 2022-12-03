from sys import stdin
readline = stdin.readline
def fab(n):
    if n <= 125:
        result = 4
    elif 126 <= n <= 211:
        result = 6
    else:
        result = 8
    return result 
n = int(readline())
print(fab(n))