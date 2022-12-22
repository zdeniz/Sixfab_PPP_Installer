#!/usr/bin/python3
import serial
import os, time

# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA1", baudrate=115200, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

cmd = "AT\r\n"
port.write(cmd.encode())
rcv = port.read(10)
print (rcv)

cmd = 'AT+IPR=460800\r\n'
port.write(cmd.encode())
time.sleep(1)
port.close()

port2 = serial.Serial("/dev/ttyAMA1", baudrate=460800, timeout=1)
time.sleep(1)

cmd = 'AT&W\r'
port2.write(cmd.encode())
rcv = port2.read(10)
print (rcv)

cmd = 'AT\r\n'
port2.write(cmd.encode())
rcv = port2.read(10)
print (rcv)

# Enable Serial Communication
port3 = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

cmd = "AT\r\n"
port3.write(cmd.encode())
rcv = port3.read(10)
print (rcv)

cmd = 'AT+IPR=460800\r\n'
port3.write(cmd.encode())
time.sleep(1)
port3.close()

port4 = serial.Serial("/dev/ttyAMA0", baudrate=460800, timeout=1)
time.sleep(1)

cmd = 'AT&W\r'
port4.write(cmd.encode())
rcv = port4.read(10)
print (rcv)

cmd = 'AT\r\n'
port4.write(cmd.encode())
rcv = port4.read(10)
print (rcv)
