import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()
server.login('khushiashta12@gmail.com','ublquatqkrzmjirr')
server.sendmail('khushiashta12@gmail.com','hemantashta001@gmail.com','This mail is send by python code')
print('mail sent successfully')

