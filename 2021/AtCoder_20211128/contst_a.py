from sys import stdin
readline = stdin.readline
def fab(n,s):
    s1 = ""
    s2 = ""
    cnt = 0
    for i in range(n):
        s1 = s[0:i] + s[i+1:]
        for j in range(i+1,n):
            s2 = s[0:j] + s[j+1:]
            if s1 == s2:
                cnt += 1
    return cnt

n = int(readline())
s = str(readline())
print(fab(n,s))
 