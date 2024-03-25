from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
a_list = list(map(int,readline().rstrip("\n").split()))
result = ""
s = 0
for i in range(n - 1):
    s = a_list[i] * a_list[i+1]
    result = result + str(s) + " "
print(result)
