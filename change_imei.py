#!/usr/bin/python3
import serial
import os, time

NEW_IMEI = "864626045757249"

# Enable Serial Communication
# port = serial.Serial("/dev/ttyAMA1", baudrate=115200, timeout=1)
port = serial.Serial("/dev/ttyAMA1", baudrate=460800, timeout=1)

cmd = "AT\r\nAT\r\n"
port.write(cmd.encode())
rcv = port.read(10).decode(encoding="utf-8")
print (rcv)
if "OK" not in rcv:
    print("AT comm error!")
    exit(-1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
cmd = "AT+CGSN=1\r\r\n"
port.write(cmd.encode())
rcv = port.read(25).decode(encoding="utf-8")
print(f"Current IMEI: {rcv}")

cmd = f'AT$QCCGSN=IMEI,{NEW_IMEI}\r'
port.write(cmd.encode())
rcv = port.read(50).decode(encoding="utf-8")
print (rcv)

print("DONE!")
