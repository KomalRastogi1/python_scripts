import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#setup port number and server name 

smtp_port = 587          #Standard secure SMTP port 
smtp_server = "smtp.gmail.com"

email_from = "komal.rastogi0007@gmail.com"
email_list = ["rastogi.m210@gmail.com", "pkp96900@gmail.com", "rastogiprince69@gmail.com"]

pswd = "egirdxqaebuaelhu"

subject = "new email from komal with attachment"

def send_emails(email_list):
    for person in email_list:
        body = f"""
        line 1 
        line 2
        line3
        """
       #make a mime object to define part of the email

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject
        
        #attach the body to the message 
        msg.attach(MIMEText(body,'plain'))
        
        #define the file to attach 
        filename = "annual-survey.csv"
        
        #open a file in python and read as binary 
        attachment = open(filename,'rb') # r for read and b for binary 
        
        #Encode as base 64
        '''The MIMEBase constructor typically takes two parameters:
            'application': This parameter specifies the top-level media type of the attachment. In this case, 'application' indicates that the attachment is a binary application data.
            'octet-stream': This parameter specifies the specific subtype of the attachment. 'octet-stream' indicates that the content of the attachment is arbitrary binary data'''
        attachment_package = MIMEBase('application','octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('content-disposition',"attachment; filename = " + filename)
        msg.attach(attachment_package)
        
        text = msg.as_string()
        
        print("connecting to the server.....")
        personal_server = smtplib.SMTP(smtp_server,smtp_port)
        personal_server.starttls()
        personal_server.login(email_from,pswd)
        print("sucessfully connected to the server")
        print()
        
        
        print(f'sending email to -{person}...')
        personal_server.sendmail(email_from, person, text)
        print(f'Email sent to:{person}')
        print()
        
    personal_server.quit()
    
    
send_emails(email_list)        
        
    