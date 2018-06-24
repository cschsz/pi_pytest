#!/usr/bin/env python3
import os
import time

min = [0] * 8
max = [0] * 8
cnt = [0] * 8
while True:
    f = open("cpuspeed.log", "a")
    try:
        stream = os.popen('grep MHz /proc/cpuinfo')
        line = stream.read()
        line = line.replace(": ", "")
        line = line.replace('\t', '\n')
        array = line.split("\n")
        buffer = time.strftime("%Y-%m-%d %H:%M:%S")
        pos = 0
        for val in array:
            try:
                buffer += ";{:4.0f}".format(float(val))
                if float(val)   >= 3800:
                    max[pos] += 1
                elif float(val) >= 1700:
                    cnt[pos] += 1
                pos += 1
            except Exception:
                pass
        #buffer += ";{:3.0f}".format(min * 100 / cnt)
        #buffer += ";" + str(max * 100 / cnt)
        print (buffer + str(cnt) + str(max))
        buffer += "\n"
        f.write(buffer)
        time.sleep(1)
    except:
        f.close()
        break
