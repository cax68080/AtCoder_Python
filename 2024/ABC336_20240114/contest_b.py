from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
counter = 0
while True:
    if n % 2 == 0:
        counter += 1
        n = n // 2
    else:
        print(counter)
        break
    if n < 2:
        print(counter)
        break


