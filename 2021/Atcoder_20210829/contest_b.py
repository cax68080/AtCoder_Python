from sys import stdin
readline = stdin.readline
def fab(n):
    a = []
    result = "No"
    for i in range(n):
        s,t = map(str,readline().split())
        a.append(s.strip()+t.strip())
    for i in range(n):
        for j in range(i+1 ,n):
            if a[i] == a[j]:
                result = "Yes"
                break
    return result

n = int(readline())
print(fab(n))