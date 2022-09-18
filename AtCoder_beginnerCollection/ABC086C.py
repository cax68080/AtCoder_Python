from sys import stdin
readline = stdin.readline
def fab(t,x,y):
    distance = abs(x + y)
    result = ""
    if t < distance:
        result = "No"
    elif t -distance == 0:
        result = "Yes"
    else:
        if (t - distance) % 2 == 0:
            result = "Yes"
        else:
            result = "No"
    return result
n = int(readline())
for i in range(n):
    t,x,y = map(int,readline().split())
    s = fab(t,x,y)
    if s == "Yes":
        continue
    else:
        break
print(s)
