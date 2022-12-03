from sys import stdin
readline = stdin.readline
n = int(readline())
bin_n = '{:b}'.format(n)
bin_n = bin_n.replace('1','2')
print(bin_n)