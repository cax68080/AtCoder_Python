from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
s = list(readline().rstrip("\n"))
#print(s)
flg_A = False
flg_B = False
flg_C = False
for i in range(n):
    if s[i] == "A":
        flg_A = True
    elif s[i] == "B":
        flg_B = True
    elif s[i] == "C":
        flg_C = True
    else:
        pass
    if flg_A and flg_B and flg_C:
        print(i + 1)
        break
