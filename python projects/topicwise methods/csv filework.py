import time
import os
import pandas
while True:
    if os.path.exists("temps.csv"):
        make= pandas.read_csv("temps.csv")
        print(make.mean())
        print(make.mean()["st1"])
    else:
        print("file not found")
    time.sleep(5)