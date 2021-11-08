import serial
import os, time
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA1", baudrate=115200, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write("AT\r\n")
rcv = port.read(10)
print (rcv)

port.write('AT+IPR=460800\r\n')
time.sleep(1)
port.close()

port2 = serial.Serial("/dev/ttyAMA1", baudrate=460800, timeout=1)
time.sleep(1)

port2.write('AT&W\r')
rcv = port2.read(10)
print rcv

port2.write('AT'+'\r\n')
rcv = port2.read(10)
print rcv


