from sys import stdin
readline = stdin.readline
h,w,x,y = map(int,readline().split())
list_cell = []
count = 1
for i in range(h):
    list_raw = list(readline().rstrip("\n"))
    list_cell.append(list_raw)
#print(list_cell)
x = x - 1
y = y - 1
for i in range(1,h):
    #print(i)
    if 0 <= x - i < h:
        if list_cell[x - i][y] == ".":
            count += 1
        else:
            break
    else:
        break
for i in range(1,h):
    #print(i)
    if 0 <= x + i < h:
        if list_cell[x + i][y] == ".":
            count += 1
        else:
            break
    else:
        break
for i in range(1,w):
    #print(i)
    if 0 <= y - i < w:
        if list_cell[x][y - i] == ".":
            count += 1
        else:
            break
    else:
        break
for i in range(1,w):
    #print(i)
    if 0 <= y + i < w:
        if list_cell[x][y + i] == ".":
            count += 1
        else:
            break
    else:
        break
print(count)

    