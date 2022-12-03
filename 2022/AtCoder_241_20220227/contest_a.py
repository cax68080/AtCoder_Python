from sys import stdin
readline = stdin.readline
n_list = list(map(int,readline().split()))
srt = 0
for i in range(3):
    n = n_list[srt]
    srt = n
print(n)
