from sys import stdin
readline = stdin.readline
n = int(readline())
day_count = 1
member_count = 0
member_list = set()
for _ in range(n):
    member_count = len(member_list)
    member = readline().rstrip('\n')
    member_list.add(member)
    if len(member_list) > member_count:
        print(day_count)
    else:
        pass
    day_count += 1
    