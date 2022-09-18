from sys import stdin
readline = stdin.readline
s = readline().rstrip('\n')
list_s = list(s)
list_n = ['0','1','2','3','4','5','6','7','8','9']
for i in list_n:
    if list_s.count(i) == 0:
        print(i)
        break
