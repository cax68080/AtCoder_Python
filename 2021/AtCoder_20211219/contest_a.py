from sys import stdin
readline = stdin.readline
def fab(s):
    s_list = list(s)
    result = int(s_list[0]) * int(s_list[2])
    return result
s = str(readline())
print(fab(s))
