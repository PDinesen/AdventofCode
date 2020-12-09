from datetime import datetime
import requests


t = datetime.now()
print(t)
timestamp = datetime.timestamp(t)
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

