# a broken work in progress:

import smtplib, bs4, requests
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

def getOaklandEvictionSched(pdfURL):
    res = requests.get(pdfURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    for link in soup.find_all(class_="btn"):
        if link.get('href') != None:
            pdfURL = link.get('href')
            downloadSched(pdfURL)

def downloadSched(pdfURL):
    res = requests.get(pdfURL)
    res.raise_for_status()
    sendSched(res.content)

def sendSched(pdfContent):
    fromaddr = "YOUREMAIL@NOTMINE.COM"
    toaddr = "YOUREMAIL@NOTMINE.COM"
   
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = toaddr 
      
    # storing the subject  
    msg['Subject'] = "My First Python Project!!"
      
    # string to store the body of the mail 
    body = "Greetings!\n\nAttached is the current Encampment Cleanup schedule published by the City of Oakland:\n"
      
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    filename = "ThisWeeksSchedule.pdf"

    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form 
    p.set_payload(pdfContent)

    # encode into base64 
    encoders.encode_base64(p) 
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login(fromaddr,"APP PASSWORD HERE") 
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
      
    # terminating the session 
    s.quit() 


getOaklandEvictionSched('https://www.oaklandca.gov/documents/homeless-encampment-clean-up-schedule')
