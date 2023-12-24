from sys import stdin
readline = stdin.readline
s = readline().rstrip("\n")
s_list = list(s)
#print(s_list)
flg_up = False
flg_low = False
flg_dif = False
for i in s_list:
    if i.isupper():
        flg_up = True
    if i.islower():
        flg_low = True
s_set = set(s_list)
if len(s_list) == len(s_set):
    flg_dif = True
if flg_up and flg_low and flg_dif:
    print("Yes")
else:
    print("No")
    