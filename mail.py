import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Camera Settings

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'arya.torabi.extraextra@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'rhxcybbgujecxeqx'  #change this to match your gmail password

#Set GPIO pins to use BCM pin numbers

#Set digital pin 17(BCM) to an input and enable the pullup

#Event to detect button press

def sendmail(recipient, subject, content):
    # Create Headers
    emailData = MIMEMultipart()
    emailData['Subject'] = subject
    emailData['To'] = recipient
    emailData['From'] = GMAIL_USERNAME

    # Attach our text data
    emailData.attach(MIMEText(content))

    # Create our Image Data from the defined image
    imageData = MIMEImage(open('image.png', 'rb').read(), 'jpg')
    imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
    emailData.attach(imageData)

    # Connect to Gmail Server
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    # Login to Gmail
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    # Send Email & Exit
    session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
    session.quit