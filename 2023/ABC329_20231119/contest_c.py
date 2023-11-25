from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
s = str(readline().rstrip("\n"))
list_s = list(s)
set_s = set(list(s))
list_letter = list(set_s)
list_cnt = [0 for i in range(len(list_letter))]
#print(n,s)
#print(len(set_s))
counter = 0
l = ""
pos = 0
for i in range(n):
    if i == 0:
        l = list_s[i]
        pos = list_letter.index(l)
        counter += 1
    else:
        if list_s[i] == l:
            counter += 1
        else:
            if list_cnt[pos] <= counter:
                list_cnt[pos] = counter
            counter = 0
            l = list_s[i]
            counter += 1
            pos = list_letter.index(l)
if list_cnt[pos] <= counter:
    list_cnt[pos] = counter

#print(list_cnt)
print(sum(list_cnt))
    

