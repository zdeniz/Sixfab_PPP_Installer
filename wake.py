import serial
import os, time

# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA1", baudrate=115200, timeout=1)

sh_cmd = "gpio -g mode 25 out"
os.system(sh_cmd)

sh_cmd = "gpio -g write 25 0"
os.system(sh_cmd)

time.sleep(1)

sh_cmd = "gpio -g write 25 1"
os.system(sh_cmd)

# time.sleep(0.001)

cmd = "AT\r\nAT\r\n"
port.write(cmd.encode())

rcv = port.read(10).decode(encoding="utf-8")
print (rcv)

time.sleep(1)

sh_cmd = "gpio -g write 25 0"
os.system(sh_cmd)


if "OK" not in rcv:
    print("AT comm error!")
    exit(-1)
    
print("DONE!")
