# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:06:24 2022

@author: Berk
"""



import serial
import numpy as np

import sys
import traceback
import datetime

x_vals=[]
y_vals=[]
xs=[]
ys=[]

date=str(datetime.datetime.now())
date=date.replace(" ",",")
date=date.replace(":",".")

serialPort=serial.Serial(port="COM5", baudrate=9600,
                              bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)
         
          
while (True):
    try:
       
        if (serialPort.in_waiting > 0):
            serialString=serialPort.readline()
            
            data=serialString.decode("utf8", errors="replace")
            
            replaced_data=data.replace("\r","")
            replaced_data=replaced_data.replace("\n","")
            # replaced_data=replaced_data.replace(":","-")
            
            print(replaced_data)
            
            # x=int(str(replaced_data[:2]))
            # y=int(str(replaced_data[3:6]))
           
            # print("x:",x)
            # print("y:",y)
            #Check State
          
                #plotting data
                                                                 
                
                         
                #Saving Data
            xs.append(datetime.datetime.now().strftime('%H:%M:%S.%f'))
            ys.append(replaced_data) 
            filename = "Pressure Values" + str(date) +".txt"
            f = open(filename, "a")
            data = str(replaced_data)
            f.write(data+"\n")
            f.close()
                                               
                                                
    except:
         print("an error occured")
         traceback.print_exc()
         serialPort.close()
         break;
sys.exit("Seri Porttan veri akışı durdu/durdulurdu !")