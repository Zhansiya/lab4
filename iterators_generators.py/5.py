n = int(input())

def allnumbers(n):
    i = n
    while i <= n and i >= 0:
        yield i
        i -= 1

for num in allnumbers(n):
    print(num)