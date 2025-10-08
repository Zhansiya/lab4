import datetime

first = datetime.datetime(2025, 4, 29, 12, 0, 0)
second = datetime.datetime(2025, 5, 30, 12, 30, 0)

difference = second - first
print(difference.total_seconds())