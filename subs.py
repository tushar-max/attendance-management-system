import pandas as pd
from datetime import datetime
import smtplib


def email_snd(ab,pre):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("eyrc.vb.2343@gmail.com", "HameshaHasteRahoJi")
    for email in ab:
        message = "Dear student,\nYou were absent in today's class.Please don't miss your classes.\nRegards,\nSubject Coordinator.\n (This is system generated message. Please contact to your faculty if you are having any issues.)"
        s.sendmail("eyrc.vb.2343@gmail.com", email, message)
    for email in pre:
        message = "Dear student,\nYour today's attendance has been marked successfully\n-Regards,\nSubject Coordinator."
        s.sendmail("eyrc.vb.2343@gmail.com", email, message)
    s.quit()

file = open('p1.txt', 'r+')
nameLst = file.readline()
nameList = list(nameLst.split(','))
nameList.pop()
df = pd.read_csv('attendance.csv', index_col=False)
di = list(df['Name'])
li = []
for i in range(len(di)):
    if di[i].upper() in nameList:
        li.append(1)
    else:
        li.append(0)

now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")
df[dt] = li
df.to_csv('attendance.csv', index=False)
ab = []
pre = []
for i in range(len(li)):
    if li[i] == 0:
        ab.append(df['Email'][i])
    else:
        pre.append(df['Email'][i])
email_snd(ab,pre)
