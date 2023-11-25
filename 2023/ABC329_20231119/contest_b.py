from sys import stdin
readline = stdin.readline
n = int(readline().rstrip("\n"))
list_a = list(map(int,readline().rstrip("\n").split()))
#print(list_a)
a = max(list_a)
count = list_a.count(a)
for _ in range(count):
    list_a.remove(a)
#print(list_a)
print(max(list_a))

