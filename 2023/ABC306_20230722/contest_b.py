from sys import stdin
readline = stdin.readline
list_a = list(map(int,readline().rstrip("\n").split()))
#print(list_a)
result = 0
num = 0
for i in list_a:
    result += i * (2 ** num)
    num += 1
print(result)