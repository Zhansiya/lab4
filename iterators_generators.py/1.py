def square(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in square(5):
    print(num ** 2)