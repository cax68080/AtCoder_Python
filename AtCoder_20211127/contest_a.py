from sys import stdin
readline = stdin.readline
def fab(s1,s2):
    result = "No"
    if s1[0] == "#" and s1[1] == "#":
        result = "Yes"
    if s2[0] == "#" and s2[1] == "#":
        result = "Yes"
    if s1[0] == "#" and s2[0] == "#":
        result = "Yes"
    if s1[1] == "#" and s2[1] == "#":
        result = "Yes"
    return result
s1 = str(readline())
s2 = str(readline())
print(fab(s1,s2))
