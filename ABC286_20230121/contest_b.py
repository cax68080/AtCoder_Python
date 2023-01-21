from sys import stdin
readline = stdin.readline
n = int(readline())
s = readline().rstrip("\n")
count = s.count("na")
#print(count)
result = s.replace("na","nya",count)
print(result)