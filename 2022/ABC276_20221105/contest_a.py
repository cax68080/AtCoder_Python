from sys import stdin
readline = stdin.readline
s = list(readline().rstrip('\n'))
#print(s)
result = -1 
for i in range(len(s) - 1,-1,-1):
    #print(s[i])
    if s[i]  == "a":
        result =  i + 1
        break
print(result)
