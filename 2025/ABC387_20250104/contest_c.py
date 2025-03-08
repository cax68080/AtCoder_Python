from sys import stdin
readline = stdin.readline
l,r = map(int,readline().rstrip("\n").split())
counter = 0
top_num = ""
num_list = []
for i in range(l,r+1):
    num_list = list(str(i))
    top_num = num_list[0]
    num_list.sort(key=None, reverse=True)
    if top_num == num_list[0] and top_num > num_list[1]:
        counter += 1
print(counter)
