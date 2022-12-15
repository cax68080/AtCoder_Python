from sys import stdin
readline=stdin.readline
def fab():
    n = int(readline())
    s = readline()
    pos = s.find("1")
    if pos % 2 == 0:
        result = "Takahashi"
    else:
        result = "Aoki"
    return result

print(fab())