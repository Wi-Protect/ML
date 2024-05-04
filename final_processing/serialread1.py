import serial

SERIAL_PORT_1 = '/dev/ttyUSB0'
SERIAL_PORT_2 = '/dev/ttyUSB1'

ser1 = serial.Serial(port=SERIAL_PORT_1, baudrate=921600,
                     bytesize=8, parity='N', stopbits=1)

ser2 = serial.Serial(port=SERIAL_PORT_2, baudrate=921600,
                     bytesize=8, parity='N', stopbits=1)


while True:
    strings1 = str(ser1.readline())
    strings2 = str(ser2.readline())
    print(strings1)
    print("---------------")
    print(strings2)