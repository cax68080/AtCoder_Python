from sys import stdin
from itertools import combinations
readline = stdin.readline
n,p,q = map(int,readline().split())
list_a = list(map(int,readline().split()))
yes_count = 0
for a,b,c,d,e in combinations(list_a,5):
    if a % p * b % p * c % p * d % p * e % p == q:
        yes_count += 1
print(yes_count)
