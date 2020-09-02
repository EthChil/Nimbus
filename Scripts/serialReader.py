import serial


ser = serial.Serial('COM', 115200);

while True:
    print(ser.read())


