from sys import stdin
readline = stdin.readline
s = readline().rstrip("\n")
t = readline().rstrip("\n")
pos = len(s) // 2
l = 0
while True:
    if len(s) > 100:
        if s[:pos] == t[:pos]:
            l = l + len(s[pos:]) - 1
            s = s[pos:]
            t = t[pos:]
            pos = len(s) // 2 
        else:
            s = s[:pos]
            t = t[:pos]
            pos = len(s) // 2
        #print(s)
        #print(t)
        #print(l)
    else:
        break
for i in range(len(t) + 1):
    if s[:i] == t[:i]:
        pass
    else:
        print(i + l)
        break
        
        
    
