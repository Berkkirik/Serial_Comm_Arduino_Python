
"""
Created on Thu Dec 29 03:57:27 2022

@author: Berk
"""


import numpy as np
import serial
import time
import datetime


xs = []
ys = []

date = str(datetime.datetime.now())
date = date.replace(" ", ",")
date = date.replace(":", ".")
start_time = time.time()


serialPort = serial.Serial(
    port="COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
while True:
    if serialPort.in_waiting > 0:
        serialString = serialPort.readline()

        data = serialString.decode("utf8", errors="replace")

        splitted_data = data.split(":")

        try:
            splitted_data[0] = int(splitted_data[0])
            splitted_data[1] = int(splitted_data[1])
        except:
            continue

        replaced_data = data.replace("\r", "")
        replaced_data = replaced_data.replace("\n", "")
        replaced_data = replaced_data.replace("\t", "")
        replaced_dataa = replaced_data.replace(":", "")
    
        current_time = time.time()
        elapsed_time = int(current_time - start_time)


        tupled_data = (splitted_data[0],splitted_data[1])
        print(tupled_data)
        xs.append(datetime.datetime.now().strftime("%H:%M:%S.%f"))
        ys.append(splitted_data)
        filename = "Pressure_Values" + str(date) + ".txt"
        f = open(filename, "a")
        data = str(
            replaced_data
            + "----------"
            + str("Your Pressure  While Operating on The Scissors " +"at the"+ str(elapsed_time)+"second"))
        f.write(data + "\n")
        f.close()



