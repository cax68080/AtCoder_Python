from sys import stdin
readline = stdin.readline
s = readline().rstrip("\n")
t = readline().rstrip("\n")
pos1 = 0
pos2 = -1
while True:
    #print(s[pos1])
    #print(t[pos1])
    #print(s[pos2])
    #print(t[pos2])
    if s[pos1] != t[pos1]:
        print(pos1 + 1)
        break
    else:
        pos1 += 1
        if len(s) < pos1 + 1:
            print(len(s) + 1)
            break
    if s[pos2] != t[pos2]:
        print(len(t) + pos2 + 1)
        break
    else:
        pos2 -= 1
        if len(s) + pos2  < 0:
            print(0)
            break 
            

