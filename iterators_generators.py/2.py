n = int(input())
def even(n):
    i = 0
    while i <= n:
        yield i
        i += 2

for i in range(0, n, 2):
    print(i, end=", ")