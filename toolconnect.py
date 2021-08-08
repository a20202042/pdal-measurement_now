import serial.tools.list_ports
import qt5test


def com2():
    port_list = list(serial.tools.list_ports.comports())
    port_list_1 = []
    if len(port_list) == 0:
        pass
    else:
        for port in serial.tools.list_ports.comports():
            port_list_1.append(str(port))
    print("可用連接COM%s" % port_list_1)
    return port_list_1


def serial_test(comnumber):
    COM_PORT = ("COM%s" % comnumber)  # 指定通訊埠名稱
    BAUD_RATES = 57600  # 設定傳輸速率
    BYTE_SIZE = 8
    PARITY = 'N'  # 校驗位
    STOP_BITS = 1
    ser = serial.Serial(COM_PORT, BAUD_RATES, BYTE_SIZE, PARITY, STOP_BITS, timeout=None)
    string_slice_start = 8
    string_slice_period = 12
    try:
        print("in try")
        while True:
            while ser.in_waiting:  # 若收到序列資料…
                data_raw = ser.read_until(b'\r')
                data = data_raw.decode()  # 用預設的UTF-8解碼
                equipment_ID = data[:string_slice_start - 1]
                altered_string = data[string_slice_start:string_slice_start + string_slice_period - 1]
                altered_int = float(altered_string)
                # print('接收到的原始資料：', data_raw)
                # print('接收到的資料：', data)
                # print('Measurement Data From : ', equipment_ID)
                # print('Altered Data : ', altered_string)
                # print('Altered Float : ', altered_int)
                unit = list(data)
                I = ("I")
                if unit[-2] == I:
                    altered_int = ("%sin" % altered_int)
                else:
                    altered_int = ("%smm" % altered_int)
                a = []
                a.append(altered_int)
                a.append(equipment_ID)
                ser.close()
                print("close")
                return a

    except:
        print("no")


def close(comnumber):
    COM_PORT = ("COM%s" % comnumber)  # 指定通訊埠名稱
    BAUD_RATES = 57600  # 設定傳輸速率
    BYTE_SIZE = 8
    PARITY = 'N'
    STOP_BITS = 1
    ser = serial.Serial(COM_PORT, BAUD_RATES, BYTE_SIZE, PARITY, STOP_BITS, timeout=None)
    string_slice_start = 8
    string_slice_period = 12
    ser.close()
