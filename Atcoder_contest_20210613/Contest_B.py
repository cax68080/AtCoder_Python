from sys import stdin
readlne = stdin.readline
def fab():
    n = int(readlne())
    a = list(map(int,readlne().split()))
    a.sort(reverse=False)
    s = 1
    result = "Yes"
    for i in range(n):
        if s == a[i]:
            s += 1
        else:
            result = "No"
            break
    return(result)
print(fab())