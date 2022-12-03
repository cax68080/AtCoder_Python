from sys import stdin
readline = stdin.readline
def dist(pos_list,pos):
    if pos == "E":
        pos_list[0] += 1
    elif pos == "S":
        pos_list[1] -= 1
    elif pos == "W":
        pos_list[0] -= 1
    elif pos == "N":
        pos_list[1] += 1
    else:
        pass
    return pos_list
def turn(pos):
    if pos == "E":
        return "S"
    elif pos == "S":
        return "W"
    elif pos == "W":
        return "N"
    elif pos == "N":
        return "E"
    else:
        return pos
def fab(n,s):
    s_list = list(s)
    pos_list = [0,0]
    pos = "E"
    for i in range(n):
        if s_list[i] == "R":
            pos = turn(pos)
        elif s_list[i] == "S":
            pos_list = dist(pos_list,pos)
    print(str(pos_list[0]) + " " + str(pos_list[1]))
n = int(readline())
s = str(readline().rstrip('\n'))
fab(n,s)