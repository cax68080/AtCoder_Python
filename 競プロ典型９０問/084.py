from sys import stdin
readline = stdin.readline
n = int(readline())
s = readline().rstrip('\n')
count_s = 0
for i in range(n):
    for j in range(i+1,n+1):
        #print(s[i:j])
        if "o" in s[i:j] and "x" in s[i:j]:
            count_s += 1
print(count_s)
