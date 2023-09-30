from sys import stdin
readline = stdin.readline
n = list(map(str,readline().rstrip("\n")))
#print(n)
result = "Yes"
for i in range(len(n) - 1):
    if int(n[i]) > int(n[i + 1]):
        pass
    else:
        result = "No"
        break
print(result)