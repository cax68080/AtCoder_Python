from sys import stdin
readline = stdin.readline
n,m,p = map(int,readline().rstrip("\n").split())
moon_count = 0
day_count = 0
day_count += m
if n >= day_count:
    moon_count += 1
    while True:
        day_count += p
        if n >= day_count:
            moon_count += 1
        else:
            break
print(moon_count)

 