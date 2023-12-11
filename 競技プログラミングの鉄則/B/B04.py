from sys import stdin
readline = stdin.readline
n = list(readline().rstrip("\n"))
answer = 0
num = len(n) - 1
for i in n:
    if i == "1" and num > 0:
        answer += 2 ** num
    elif i == "1" and num == 0:
        answer += 1
    else:
        pass
    num -= 1
print(answer)

