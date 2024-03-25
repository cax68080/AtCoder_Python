from sys import stdin
readline = stdin.readline
s = str(readline().rstrip("\n"))
cap_str = s.capitalize()
if s == cap_str:
    print("Yes")
else:
    print("No")
    