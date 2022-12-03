from sys import stdin
readline = stdin.readline
s = str(readline().rstrip('\n'))
t = str(readline().rstrip('\n'))
len_s = len(s)
len_t = len(t)
if len_s < len_t:
    print('No')
elif len_s == len_t:
    if s == t:
        print('Yes')
    else:
        print('No')
else:
    result = 'No'
    for i in range(len_s):
        #print(s[i:i + len_t] )
        if s[i:i + len_t] == t:
            result = 'Yes'
            break
    print(result)
