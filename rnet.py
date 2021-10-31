import serial
import time  

# Enabling Serial Communication
sp = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    timeout=1)

