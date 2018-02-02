RPI-FadeAway
============

The codes here are prepared on a raspberry pi 3.
This is conversion of the code Fadeaway by mrichardson23, destined intitially for the Arduino.
It is converted to Python and uses the adafruit driver PCA9685 to manage servo control.

First run the following commands:
sudo apt-get install python-pip
sudo pip install adafruit-pca9685

The code test-servo-range.py is destined as a first test with your servo motors.
This is for testing the given servo's range. Run the code and take note of lowest and highest numbers to which the motor responds.

References:
https://github.com/mrichardson23/FadeAway
https://github.com/adafruit/Adafruit_Python_PCA9685/
