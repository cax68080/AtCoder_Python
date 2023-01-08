from sys import stdin
readline = stdin.readline
t = int(readline())
def get_odd_count(n,num_list):
    count = 0
    for i in num_list:
        if i % 2 == 1:
            count += 1
        else:
            pass
    return count

for _ in range(t):
    n = int(readline())
    list_a = list(map(int,readline().split()))
    result = get_odd_count(n,list_a)
    print(result)
    
