from sys import stdin
readline = stdin.readline
n,d = map(int,readline().rstrip("\n").split())
snake_list = []
snake = []
for i in range(n):
    snake = list(map(int,readline().rstrip("\n").split()))
    snake_list.append(snake)
#print(snake_list)
l = 0
k = 1
for l in range(d):
    for j in range(n):
        s = snake_list[j][0] * (snake_list[j][1] +k) 
        if l < s:
            l = s
    k += 1
    print(l)
