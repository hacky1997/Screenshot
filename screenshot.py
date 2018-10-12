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
# def sendmail(self,file):
# mail = smtplib.SMTP('smtp.gmail.com',587)

# mail.ehlo()

# mail.starttls()

# mail.login('sayaknaskar@gmail.com','8697925188')

# mail.sendmail('sayaknaskar@gmail.com','naskar.sukumar.12@gmail.com',ss())

# mail.close()
