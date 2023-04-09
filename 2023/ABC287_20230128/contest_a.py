from sys import stdin
readline = stdin.readline
n = int(readline())
count_for = 0
count_against = 0
for _ in range(n):
    s = readline().rstrip('\n')
    if s == "For":
        count_for += 1
    else:
        count_against += 1
if count_for > count_against:
    print("Yes")
else:
    print("No")