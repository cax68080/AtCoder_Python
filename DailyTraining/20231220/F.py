from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
result = ""
while True:
    if n > 0:
        if n % 2 == 0:
            result = "B" + result
            n = n // 2
        else:
            result = "A" + result
            n = n - 1
    else:
        break
print(result)


