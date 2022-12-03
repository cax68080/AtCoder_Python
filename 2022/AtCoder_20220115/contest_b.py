from sys import stdin
readline = stdin.readline
def fab(n,std_list):
    pos = 0
    for i in range(n):
        if std_list[i] > pos:
            pos = std_list[i]
        else:
            break
    return pos
n = int(readline())
std_list = list(map(int,readline().split()))
print(fab(n,std_list))