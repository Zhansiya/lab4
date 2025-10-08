import datetime
import math
first = datetime.datetime(2025, 4, 29, 12, 0, 0)
second = datetime.datetime(2025, 5, 28, 12, 30, 0)

difference = second - first
print(abs(difference.total_seconds()))