from io import StringIO
import serial
import csv

DATA_COLUMNS_NAMES = ["type", "id", "mac", "rssi", "rate", "sig_mode", "mcs", "bandwidth", "smoothing", "not_sounding", "aggregation", "stbc", "fec_coding",
                      "sgi", "noise_floor", "ampdu_cnt", "channel", "secondary_channel", "local_timestamp", "ant", "sig_len", "rx_state", "len", "first_word", "data"]


SERIAL_PORT_1 = '/dev/ttyUSB0'
SERIAL_PORT_2 = '/dev/ttyUSB1'

ser1 = serial.Serial(port=SERIAL_PORT_1, baudrate=921600,
                     bytesize=8, parity='N', stopbits=1)

ser2 = serial.Serial(port=SERIAL_PORT_2, baudrate=921600,
                     bytesize=8, parity='N', stopbits=1)


while True:
    strings1 = str(ser1.readline())
    strings2 = str(ser2.readline())
    if not strings1 or not strings2:
        continue

    strings1 = strings1.lstrip('b\'').rstrip('\\r\\n\'')
    strings2 = strings2.lstrip('b\'').rstrip('\\r\\n\'')
    index1 = strings1.find('CSI_DATA')
    index2 = strings2.find('CSI_DATA')

    if index1 == -1 or index2 == -1:
        continue

    csv_reader1 = csv.reader(StringIO(strings1))
    csv_reader2 = csv.reader(StringIO(strings2))
    csi_data1 = next(csv_reader1)
    csi_data2 = next(csv_reader2)

    if len(csi_data1) != len(DATA_COLUMNS_NAMES) or len(csi_data2) != len(DATA_COLUMNS_NAMES):
        print("element number is not equal")
        continue

    print('CSI_DATA_1')
    print(csi_data1)
    print("--------------------------")
    print('CSI_DATA_2')
    print(csi_data2)
    print("--------------------------")
