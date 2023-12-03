from sys import stdin
readline = stdin.readline
n,s,m,l = map(int,readline().rstrip("\n").split())
s_cnt = 6
m_cnt = 8
l_cnt = 12
total = 0
result = 0
for i in range(n // s_cnt + 1):
    result += s_cnt