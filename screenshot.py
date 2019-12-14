from mss import mss
import smtplib
import sys,os

with mss() as sct:
    sct.shot()
    
# sct.image
# sct.monitor
file = sct.save(mon=1)
next(file)

# filepath =  '/tmp/'
# file.save        
# save = str(mss())     
#open(save, "r")        
