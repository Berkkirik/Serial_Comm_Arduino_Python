# Serial_Comm_Arduino_Python
 Serial Port Coımmunucation+ Data Visualization ( Arduino - Python)
For more information , do not hesisate to ask me via mail 




My Contact Mail :berkkirik.1999@gmail.com       or        berk.kirik@outlook.com


# Using Mu Editor , Data Visualization Part (Laparoskopi Experiment.py is related to data visualization part with Mu editor)
## (Laparoskopi Experiment.py is related to data visualization part with Mu editor)





# İMPORT SECTİON
## For more inf. about libraries (https://pypi.org/)


```
import numpy as np 
import serial
import time 
import datetime
```


# Create x_serial and y_serial lists 
## x_serial represented as xs , y_serial represented as ys



```
xs = []
ys = []
```


# For filename , get info local time and write on your file as addiction of filename
```
date = str(datetime.datetime.now())
```


# For replace unnecessary elements which came from Serial Port 
## İn my project serial port device is arduino


```
date = date.replace(" ", ",")
date = date.replace(":", ".")

```


# For Serial Port Communucation 
## Check your Comport which you connect Mıcroprocessor to your device (Which Comport is active )

```
serialPort = serial.Serial(
    port="COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


```


# While loop for append the list elements to tuppled data ( try-except block to add element into tupple)

```
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

```