from sys import stdin
readline = stdin.readline
x = int(readline().rstrip("\n"))
str_x = ""
if x > 0:
    str_x = str(x)
    if str_x[-1]  == "0":
        print(x // 10)
    else:
        print(x // 10 + 1)
else:
    str_x = str(x)
    if str_x[-1]  == "0":
        print(x // 10)
    else:
        print(x // 10 + 1)
