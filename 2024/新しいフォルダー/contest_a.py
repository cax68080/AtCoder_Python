from sys import stdin
readline = stdin.readline
s = readline().rstrip("\n")
set_s = set(s)
list_s = list(s)
for i in set_s:
    if list_s.count(i) == 1:
        result = list_s.index(i)
print(result + 1)
