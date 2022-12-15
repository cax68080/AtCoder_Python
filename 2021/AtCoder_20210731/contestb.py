from sys import stdin
readline = stdin.readline
def fab(x):
    result = "Strong"
    if x[0] == x[1] == x[2] == x[3]:
        result = "Weak"
        
    cnt = 0
    for i in range(3):
        k = i + 1
        if x[i] == "9":
            if x[k] == "0":
                cnt += 1
        else:
            if int(x[k]) == int(x[i]) + 1:
                cnt += 1
    if cnt == 3:
        result = "Weak"
    return result
x = str(readline())
print(fab(x))