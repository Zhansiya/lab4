import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(yesterday.strftime("%d.%m.%Y"))
print(today.strftime("%d.%m.%Y"))
print(tomorrow.strftime("%d.%m.%Y"))