#!/usr/bin/python3
for i in range(1, 90):
    if i / 10 > j % 10:
        continue
    else:
        if (i != 89):
            print("{:02}".format(i), end=", ")
        else:
            print("{}".format(i))