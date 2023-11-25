from sys import stdin
readline = stdin.readline
h,w = map(int,readline().split())
for _ in range(h):
    s = str(readline().rstrip("\n"))
    #rint(s)
    list_s = list(s)
    #print(list_s)
    for i in range(len(list_s) - 1):
        if list_s[i]  == "T" and list_s[i + 1]  == "T":
            list_s.pop(i)
            list_s.insert(i,"P")
            list_s.pop(i + 1)
            list_s.insert(i + 1,"C")
            #print("check")
    print("".join(list_s))
    list_s = []
    s = ""

