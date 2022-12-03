from sys import stdin
readline = stdin.readline
result = "Yes"
h = "0"
sb = "0"
tb = "0"
hr = "0"
for i in range(4):
    s = str(readline()).strip()
    if s == "H":
        if h == "0":
            h = "1"
        else:
            result = "No"
            break
    elif s == "2B":
        if sb == "0":
            sb = "1"
        else:
            result = "No"
            break
    elif s == "3B":
        if tb == "0":
            tb = "1"
        else:
            result = "No"
            break
    elif s == "HR":
        if hr == "0":
            hr = "1"
        else:
            result = "No"
            break
    else:
        continue
print(result)

