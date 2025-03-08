from sys import stdin
import math
readline = stdin.readline
n = int(readline())
#answer = 0
i = 1
max_i = int(math.sqrt(n))

answer = -1
for i in range(1, max_i + 1):
    if i * (i + 1) == n:
        answer = i + 1
        break

print(answer)
#while True:
#    answer = i * (i + 1)
#    if answer == n:
#        print(i + 1)
#        break
#    else:
#        i += 1
#        if answer > n:
#            print(-1)
#            break