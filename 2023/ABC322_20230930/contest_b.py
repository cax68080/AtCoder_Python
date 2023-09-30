from sys import stdin
readline = stdin.readline
n,m = map(int,readline().rstrip("\n").split())
s = str(readline().rstrip("\n"))
t = str(readline().rstrip("\n"))
last_len = 0 - len(s)
#print(t[:len(s)])
#print(t[last_len:])
if t[:len(s)] == s and t[last_len:] == s:
    print("0")
elif t[:len(s)] == s:
    print("1")
elif t[last_len:] == s:
    print("2")
else:
    print("3")