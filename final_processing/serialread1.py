import serial

SERIAL_PORT_1 = '/dev/ttyUSB0'

ser1 = serial.Serial(port=SERIAL_PORT_1, baudrate=921600,
                     bytesize=8, parity='N', stopbits=1)


while True:
    strings1 = ser1.readline().decode('utf-8')
    print(strings1)