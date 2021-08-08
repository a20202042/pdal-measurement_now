import serial.tools.list_ports
import serial
COM_PORT = 'COM6'  # 指定通訊埠名稱
BAUD_RATES = 2000000  # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)  # 初始化序列通訊埠

try:
    while True:
        while ser.in_waiting:  # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()  # 用預設的UTF-8解碼
            print('接收到的原始資料：', data_raw)
            print('接收到的資料：', data)

except KeyboardInterrupt:
    while True:
        while ser.in_waiting:  # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()  # 用預設的UTF-8解碼
            print('接收到的原始資料：', data_raw)
            print('接收到的資料：', data)
    ser.close()  # 清除序列通訊物件