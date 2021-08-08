def serial_test():
    print('111')
    import serial, io
    COM_PORT = 'COM4'  # 指定通訊埠名稱
    BAUD_RATES = 57600  # 設定傳輸速率
    BYTE_SIZE = 8
    PARITY = 'N'
    STOP_BITS = 1
    ser = serial.Serial(COM_PORT, BAUD_RATES, BYTE_SIZE, PARITY, STOP_BITS, timeout=None)  # 初始化序列通訊埠

    string_slice_start = 8
    string_slice_period = 12
    try:
        while True:
            while ser.in_waiting:  # 若收到序列資料…
                data_raw = ser.read_until(b'\r')
                data = data_raw.decode()  # 用預設的UTF-8解碼
                equipment_ID = data[:string_slice_start - 1]
                altered_string = data[string_slice_start:string_slice_start + string_slice_period - 1]
                altered_int = float(altered_string)
                print('接收到的原始資料：', data_raw)
                print('接收到的資料：', data)
                print('Measurement Data From : ', equipment_ID)
                print('Altered Data : ', altered_string)
                print('Altered Float : ', altered_int)
                break



    #
    # try:
    #     while True:
    #         while ser.in_waiting:
    #             sio.flush()
    #             data_raw = ser.readline()
    #             #data = data_raw.decode()
    #             print('接收到的原始資料：', data_raw)
    #             #print('接收到的資料：', data)

    except KeyboardInterrupt:
        ser.close()  # 清除序列通訊物件
        print('再見！')

# if __name__ == '__main__':
#     serial_test()