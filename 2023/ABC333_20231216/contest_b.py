from sys import stdin
readline = stdin.readline
line_table = ["AB","BC","CD","DE","EA","AE","ED","DC","CB","BA"]
s = str(readline().rstrip("\n"))
t = str(readline().rstrip("\n"))
if (line_table.count(s) > 0) and (line_table.count(t) > 0):
    print("Yes")
elif (line_table.count(s) == 0) and (line_table.count(t) == 0):
    print("Yes")
else:
    print("No")