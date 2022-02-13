import RPi.GPIO as GPIO
import time
import smtplib

from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime

datetimeobj = datetime.now()

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587 

#Sender Gmail Account Info
GMAIL_USERNAME = '#####'
GMAIL_PASSWORD = '#####'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led_pin = 17
pir_pin = 27

GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

camera = PiCamera()

print("CCTV Active")

class Emailer:
    def sendmail(self, recipient, subject, content, image, datetimeobj):
         
        #Create Headers
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = recipient
        emailData['From'] = GMAIL_USERNAME

        #Attach our text data
        emailData.attach(MIMEText(content))
        
        #Create Image Data from the Defined image
        imageData = MIMEImage(open(image, 'rb').read(), 'jpg')
        imageData.add_header('Content-Despostion', 'attachment; filename="image.jpg"')
        emailData.attach(imageData)
 
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
 
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
 
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit
 
sender = Emailer()

sendTo = '####'
emailSubject = "Motion Detected"
emailContent = "####"

#sender.sendmail(sendTo, emailSubject, emailContent) 

def my_callback(pir_pin):
    camera.start_preview()
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.5)
	
	#Image saved location on Pi
    image = '####'
    camera.capture(image)
    time.sleep(0.5)
    camera.stop_preview()
    GPIO.output(led_pin, GPIO.LOW)
    sender.sendmail(sendTo, emailSubject, emailContent, image, datetimeobj)
    print("Email Sent")
    
time.sleep(2)

try:
    GPIO.add_event_detect(pir_pin , GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print ("Finish...")
GPIO.cleanup()
