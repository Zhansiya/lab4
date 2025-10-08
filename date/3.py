import datetime 

x = datetime.datetime.now()
microsec = x.replace(microsecond=0)
print(x)
print(microsec)