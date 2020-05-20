# -*- coding: utf-8 -*-
#!/usr/sh
#!/usr/bin/env python
from futsal_python import get_date as get_futsal_date
from futsal_python import get_date_format as date_format
#from save import save_to_file
from email.mime.text import MIMEText
from email.header import Header
import smtplib

NAME = ('신천 풋살장 A', '신천 풋살장 B','신천구장')

smtp = smtplib.SMTP('smtp.gmail.com', 587)

smtp.starttls()

smtp.login('mcyoo247@gmail.com', 'yolplsbaccygbars')

futsal_date = get_futsal_date()
print(futsal_date)

#메일 내용 포멧팅
text = ''
for i in range(0,len(futsal_date)):
    text += '\n' + NAME[i]
    for j in futsal_date[i]:
        text += j + ' '

f = open("/root/futsal_python/save.txt", 'r')
text_temp = f.read()
f.close()

if text != text_temp:
    #메일 전송
    msg = MIMEText(text, "plain", "utf-8")
    msg['Subject'] = Header('축구 자리 조회', 'utf-8')
    send_to = ['ckddnd1995@naver.com','dbwptjr247@naver.com']
    msg['To'] = ", ".join(send_to)
    smtp.sendmail('mcyoo247@gmail.com', send_to , msg.as_string())

    #내용 저장
    f = open("/root/futsal_python/save.txt", 'w')
    f.write(text)
    f.close()
smtp.quit()
#save_to_file(indeed_jobs)