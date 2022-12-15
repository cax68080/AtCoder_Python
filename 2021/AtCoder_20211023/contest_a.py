from sys import stdin
readline = stdin.readline
s = str(readline().rstrip('\n'))
#print(s[-3:])
if s[-2:] == "er":
    print("er")
if s[-3:] == "ist":
    print("ist")
