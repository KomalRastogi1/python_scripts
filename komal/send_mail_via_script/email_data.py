import smtplib, ssl

#setup port number and server name 

smtp_port = 587          #Standard secure SMTP port 
smtp_server = "smtp.gmail.com"

email_from = "komal.rastogi0007@gmail.com"
email_to = "email address of sender"

pswd = " app password of gmail account of sender"
#content of the message 

message = "Dear komal, this is the first sample email"

simple_email_context = ssl.create_default_context()

try: 
    print("connecting to the smtp server ")
    personal_server = smtplib.SMTP(smtp_server,smtp_port)
    personal_server.starttls(context=simple_email_context)
    personal_server.login(email_from,pswd) 
    print("connected to the server")
    
    print(f"Sending email to -  {email_to}")
    personal_server.sendmail(email_from, email_to, message)
    print(f"Sending email from -  {email_from}")
    
except Exception as e:
    print(e)

finally:
    personal_server.quit()    

