from io import StringIO
import json
import serial
import csv
import datetime
import numpy as np
import csv
from io import StringIO
import json
from math import sqrt, atan2
import serial
import joblib
import pywt
import pandas as pd
import time


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

    try:
        csi_raw_data1 = json.loads(csi_data1[-1])
        csi_raw_data2 = json.loads(csi_data2[-1])
    except json.JSONDecodeError:
        print(f"data is incomplete")
        continue

    if len(csi_raw_data1) != 128 and len(csi_raw_data1) != 256 and len(csi_raw_data1) != 384:
        print(f"element number is not equal: {len(csi_raw_data1)}")
        continue

    if len(csi_raw_data2) != 128 and len(csi_raw_data2) != 256 and len(csi_raw_data2) != 384:
        print(f"element number is not equal: {len(csi_raw_data2)}")
        continue

    print('CSI_DATA_1')
    print(csi_raw_data1)
    print("--------------------------")
    print('CSI_DATA_2')
    print(csi_raw_data2)
    print("--------------------------")

    imaginary1 = []
    real1 = []
    imaginary2 = []
    real2 = []
    amplitudes = []
    phases = []

    for i in range(len(csi_raw_data1)):
        if i % 2 == 0:
            imaginary1.append(csi_raw_data1[i])
        else:
            real1.append(csi_raw_data1[i])

    for i in range(len(csi_raw_data2)):
        if i % 2 == 0:
            imaginary2.append(csi_raw_data2[i])
        else:
            real2.append(csi_raw_data2[i])

    # Transform imaginary and real into amplitude and phase
    for i in range(int(len(csi_raw_data1) / 2)):
        amplitudes.append(sqrt(imaginary1[i] ** 2 + real1[i] ** 2))
        phases.append(atan2(imaginary1[i], real1[i]))

    for i in range(int(len(csi_raw_data2) / 2)):
        amplitudes.append(sqrt(imaginary2[i] ** 2 + real2[i] ** 2))
        phases.append(atan2(imaginary2[i], real2[i]))
