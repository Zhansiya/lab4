a = int(input())
b = int(input())

def squares(a, b):
    while a <= b:
        x = a ** 2
        yield x
        a += 1

for x in squares(a, b):
    print(x)