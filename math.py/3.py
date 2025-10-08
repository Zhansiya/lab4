import math
sides = int(input())
length = int(input())
perimeter = sides * length
apothem = length / (2 * math.tan(math.pi/sides))
area = int((perimeter * apothem) / 2)
print(area)