from sys import stdin
readline = stdin.readline
s = list(str(readline().rstrip("\n")))
result = "Yes"
for i in range(len(s)):
    if (i + 1) % 2 == 0:
        if s[i] == "0":
            pass
        else:
            result = "No"
            break
print(result)