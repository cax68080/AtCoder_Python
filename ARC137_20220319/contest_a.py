from sys import stdin
readline = stdin.readline
def prime(s):
    result = True
    if s != 2:
        for j in range(s):
            if j > 1 and j < s:
                if s % j == 0:
                    result = False
                    break
            elif j == s:
                result = False
                break
    return result

l,r = map(int,readline().split())
num_max = 0
num_min = 0
for i in range(l,r + 1):
    if prime(i) == True:
        num_min = i
        break
for i in range(r,l,-1):
    if prime(i) == True:
        num_max = i
        break
print(num_min)
print(num_max)
print(num_max - num_min)


