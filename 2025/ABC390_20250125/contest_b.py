from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
list_s = list(map(int, readline().rstrip("\n").split()))
g = 0.0
result = "Yes"
if n <= 2:
    pass
else:
    for i in range(len(list_s)-2):
        if  list_s[i+1]**2 == list_s[i]*list_s[i+2]:
            pass
        else:
            result = "No"
            break
print(result)