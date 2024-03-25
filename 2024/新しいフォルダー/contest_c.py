from sys import stdin
from string import ascii_lowercase
readline = stdin.readline
n = int(readline().rstrip("\n"))
s = str(readline().rstrip("\n"))
mapping_from = ascii_lowercase
mapping_to = ascii_lowercase
q = int(readline().rstrip("\n"))
#print(s)
for _ in range(q):
    c,d = map(str,readline().rstrip("\n").split())
    mapping_to = mapping_to.replace(c,d)
print(s.translate(str.maketrans(mapping_from, mapping_to)))

