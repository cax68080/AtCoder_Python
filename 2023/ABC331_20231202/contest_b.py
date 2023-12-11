from sys import stdin
readline = stdin.readline
n,s,m,l = map(int,readline().rstrip("\n").split())
s_cnt = 6
m_cnt = 8
l_cnt = 12
total = 0
result = 10000000
for i in range(101):
    for j in range(101):
        for k in range(101):
            if n <= i * 6 + j * 8 + k * 12:
                result = min(result,s * i + m * j + l *k)
print(result)