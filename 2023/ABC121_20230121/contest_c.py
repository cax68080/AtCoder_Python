from sys import stdin
readline = stdin.readline
n,m = map(int,readline().split())
m_list = []
a_list = []
for _ in range(n):
    a_list = list(map(int,readline().split()))
    m_list.append(a_list)
m_list.sort(key=None,reverse=False)
for i in range(n):
    if 
