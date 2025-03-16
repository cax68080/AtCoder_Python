from sys import stdin
readline = stdin.readline
s = list(readline().rstrip("\n"))
r = []
chk = "i"
count = 0
for j in range(len(s)):
    if s[j] != chk:
        count += 1
        r.append(chk)
        r.append(s[j])
    else:
        r.append(s[j])
        if chk == "i":
            chk = "o"
        elif chk == "o":
            chk = "i"
        else:
            pass
    
if len(r) % 2 != 0:
    count += 1
    r.append("o")
#print("".join(r))
print(count)

        