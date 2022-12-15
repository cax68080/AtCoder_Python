s = input()
l = len(s)
s2 = ""
for i in range(l):
    if s[i] == "6":
        s2 = "9" + s2
    elif s[i] == "9":
        s2 = "6" + s2
    else:
        s2 = s[i] + s2
print(s2)


