from sys import stdin
readline = stdin.readline
def fab(a):
    A = [ 'ABC' , 'ARC' , 'AGC' , 'AHC' ]
    for i in A:
        if a.count(i) == 0:
            result = i
    return result
a = []
for _ in range(3):
    s = str(readline()).replace('\n', '')
    a.append(s)
print(fab(a))

