from sys import stdin
readline = stdin.readline
def fab():
    n = int(readline())
    l =[]*n
    for i in range(n):
        l.append(int(readline()))
    l.sort(reverse=False)
    s = 0
    t = 0
    r1 = 0
    r2 = 0
    p = 1
    for i in range(n):
        s = l[i]
        if s == t and r1 == 0 :
            r1 = s
        else:
            t = s
        if s != p and r2 == 0:
            r2 = p
        else:
            p += 1
    if r1 == 0 and r2 == 0:
        return "Correct"
    else:
        return str(r1) + " " + str(r2)
print(fab())
