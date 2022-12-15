from sys import stdin
readline = stdin.readline
s = readline().rstrip('\n')
s_list = list(s)
#print(s_list)
chk_upper = "0"
chk_lower = "0"
chk_dup = "0"
for i in s_list:
    if i.isupper():
        chk_upper = "1"
    if i.islower():
        chk_lower = "1"
    if s_list.count(i) > 1:
        chk_dup = "1"
        break
#print(chk_upper)
if chk_lower == "1" and chk_upper == "1" and chk_dup == "0":
    print("Yes")
else:
    print("No")

 
