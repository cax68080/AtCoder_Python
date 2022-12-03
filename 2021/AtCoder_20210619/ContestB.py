from sys import stdin
readline = stdin.readline
def fab(n):
    price = int(n)
    i = 0
    x = 0
    while price > x:
        i += 1
        x = x + i
    return(i)
print(fab(int(readline())))