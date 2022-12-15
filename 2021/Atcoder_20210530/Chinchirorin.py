from sys import stdin
readline = stdin.readline
def fab(dlist):
    if dlist[0] == dlist[1]:
        print(dlist[2])
    elif dlist[0] == dlist[2]:
        print(dlist[1])
    elif dlist[1] == dlist[2]:
        print(dlist[0])
    else:
        print("0")
    
l = list(map(int,readline().split()))
fab(l)
