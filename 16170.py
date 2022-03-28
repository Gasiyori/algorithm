from datetime import datetime

time = str(datetime.utcnow())

time = time.split()[0]

print(time.split("-")[0])
print(time.split("-")[1])
print(time.split("-")[2])