import smtplib
from email.mime.text import MIMEText
  
# third-part smtp service
mail_host = "applesmtp.126.com"  # SMTP server
mail_user = "eric_python_auto@126.com"  # user name
mail_pass = "qijzxcqj00838488"  # passcode
  
sender = 'eric_python_auto@126.com'  # sender
receivers = ['imaginechen@126.com', 'eric_python_auto@126.com']  # reciever
  
  
content = 'Python Send Mail !'
title = 'Python SMTP Mail'  # title
message = MIMEText(content, 'plain', 'utf-8')  # content
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title
  
try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # Launch SSL, general port 465
    smtpObj.login(mail_user, mail_pass)  # login authorization
    smtpObj.sendmail(sender, receivers, message.as_string())  # send out the message
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)