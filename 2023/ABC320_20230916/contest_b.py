from sys import stdin
readline = stdin.readline
s = readline().rstrip("\n")
len_s = 0
for i in range(len(s)):
    for j in range(i,len(s) + 1):
        if s[i:j] == "".join(reversed(s[i:j])):
            if len(s[i:j]) > len_s:
                 len_s = len(s[i:j])
print(len_s)
