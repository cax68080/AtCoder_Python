def fib():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(key=None,reverse=True)
    b.sort(key=None,reverse=True)
    st =0
    for i in range(n):
        st += abs(a[i] - b[i])
    return st
print(fib())