from sys import stdin
from collections import Counter
readline = stdin.readline
s = str(readline().rstrip('\n'))
s_counter =Counter(s)
s_item = sorted(s_counter)
#print(s_counter)
#print(s_item)
t =s_item[0]
#print(s_counter[t])
#print(t)
r = ""
cnt = 0
result = ""
for i in range(len(s_item)):
    r = s_item[i]
    cnt = s_counter[r]
    result = result + r * cnt
print(result)
