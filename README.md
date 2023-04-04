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