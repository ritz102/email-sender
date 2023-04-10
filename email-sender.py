import smtplib # Simple Mail Transfer Protocol (SMTP), helps send an mail to an internet machine.

import ssl #Secure Sockets Layer (SSL), helps in establishing an encrypted link between the server and the client
from email.message import EmailMessage

sender_email = 'sendingemail@gmail.com' #Gmail account that the email will be sent from.
google_apps_password = '16digitkeyfromgoogle' # This key is unique for every google account.
reciverers_email = 'recievingemail@gmail.com' #Gmail account that the email will be recieved to.

subject = 'Testing'
body = """Testing an Automated python gmail system """

context = ssl.create_default_context() #establishes the secure connection between the client and server over the internet.

em = EmailMessage() # enables the EmailMessage class in python by assigning it to the em variable
em['From'] = sender_email
em['To'] = reciverers_email
em['Subject'] = subject
em.set_content(body)



with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, google_apps_password) # Logs in and establishes a secure connection with the STMP server and authorizes sender to send emails
    smtp.sendmail(sender_email, reciverers_email, em.as_string()) # Sends over the email in a string format

