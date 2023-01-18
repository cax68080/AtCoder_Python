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
    if list_cell[y][i] == ".":
        count += 1
    else:
        break
for i in range(x + 1,w + 1,1):
    print(i)
    if list_cell[y][i] == ".":
        count += 1
    else:
        break
for i in range(y - 1,-1,-1):
    #print(i)
    if list_cell[i][x] == ".":
        count += 1
    else:
        break
for i in range(y + 1,h + 1,1):
    #print(i)
    if list_cell[i][x] == ".":
        count += 1
    else:
        break
print(count)

    