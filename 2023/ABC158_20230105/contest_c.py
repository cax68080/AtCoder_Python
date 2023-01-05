from sys import stdin
readline = stdin.readline
max_a = 1001
a,b = map(int,readline().split())
for result in range(1,max_a):
    tax_a = int(result * 0.08) 
    tax_b = int(result * 0.1)
    if (tax_a == a) and (tax_b == b):
        break
    else:
        result = -1
print(result)