n = int(input())

def division(n):
    i = 0
    while i <= n:
        yield i
        i += 1
    if ( i % 3 == 0 and i % 4 == 0):
            print(i)

for num in division(n):
     if ( num % 3 == 0 and num % 4 == 0):
          print(num)