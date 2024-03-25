from sys import stdin
readline = stdin.readline
list_s = list(readline().rstrip("\n"))
result = "Yes"
if list_s[0] == "<":
    if list_s[-1] == ">":
        for i in range(len(list_s)):
            if i > 0 and i < len(list_s) - 1 and list_s[i] != "=":
                result = "No"
                break
    else:
        result = "No"
else:
    result = "No"
print(result)