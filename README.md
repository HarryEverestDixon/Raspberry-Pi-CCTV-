# Raspberry-Pi-CCTV-
You will need: An email address with full access to be the sender and another for a recipeient
               Raspberry Pi
               sensor Module
               Camera Module

Python program to be used on a Raspberry Pi like the Raspberry Pi Zero W.
When a Sensor in my case a Passive Infrared Sensor(PIR) HC-SR501 is attched to the corresponding pins of the Pi and a Camera module is also attcached an image will be taken and stored to a custom directory on the Pi, the program will then fetch the image and using simple mail transfer protycol(SMTP) will send the image from the address sued for the sender to a designated adress to be the recipient.
