from sys import stdin
readline = stdin.readline
s = list(readline().rstrip('\n'))
#s_sort = sorted(s)
t = list(readline().rstrip('\n'))
#t_sort = sorted(t)
dif_str = ""
pos = 0
ex = 0
for i in range(len(s)):
    if s[i] == t[i+ex]:
        continue
    else:
        dif_str = t[i]
        ex = 1
        pos = i + 1
        break
if dif_str == "":
    #dif_str = t[-1]
    print(len(t))
else:
    print(pos)
