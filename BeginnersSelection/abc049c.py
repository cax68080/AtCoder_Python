from sys import stdin
redline = stdin.readline
s_list = ["eraser","erase","dreamer","dream"]
s = redline().rstrip('\n')
for i in s_list:
    s = s.replace(i,"")
if len(s) == 0:
    print("YES")
else:
    print("NO")
