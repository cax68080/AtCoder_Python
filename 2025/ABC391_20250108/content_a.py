from sys import stdin
readline = stdin.readline
d = readline().rstrip("\n")
if d == "N":
    print("S")
elif d == "S":
    print("N")
elif d == "W":
    print("E")
elif d == "E":
    print("W")
elif d == "NE":
    print("SW")
elif d == "NW":
    print("SE")
elif d == "SE":
    print("NW")
elif d == "SW":
    print("NE")
else:
    print("error")