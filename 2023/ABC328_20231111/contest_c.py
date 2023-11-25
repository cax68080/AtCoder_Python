from sys import stdin
readline = stdin.readline
n,q = map(int,readline().rstrip("\n").split())
s = str(readline().rstrip("\n"))
s_list = list(s)
a_list = []
b_list = [0]
counter = 0
for i in range(len(s_list)-1):
    if s_list[i] == s_list[i + 1]:
        a_list.append(1)
    else:
        a_list.append(0)
#print(a_list)
for i in range(len(a_list)):
    counter += a_list[i]
    b_list.append(counter)
#print(b_list)
for i in range(q):
    l,r = map(int,readline().rstrip("\n").split())
    print(b_list[r - 1] - b_list[l - 1])


