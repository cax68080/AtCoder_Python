from sys import stdin
readline = stdin.readline
s = readline().rstrip("\n")
s = s.replace("0","2")
s = s.replace("1","0")
s = s.replace("2","1")
print(s)