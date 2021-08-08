import json
import global_var as gvar


def write():
    numbers = {
        "sql": {
            "host": "163.18.69.14",
            "name": "pdal-measurement",
            "user": "root",
            "charset": "utf8",
            "password": "rsa+0414018"
        },
        "measure_tool": {
            "number": 3,
            "id": {
                "COM1": "",
                "COM2": "",
                "COM3": ""
            }
        }
    }
    filename = "system.json"  # 指定要把numbers串列存到number.json檔中
    with open(filename, "w") as file:  # 以寫入模式開啟檔案才可以將資料儲存進去
        json.dump(numbers, file)  # 將numbers串列存到number.json檔


# def open_json():
#     filename = "system.json"  # 這行我們要確定是不是跟前面的讀取檔案名稱相同
#     with open(filename) as file:  # 以讀取模式開啟檔案(若沒有第二個參數都是預設成讀取模式)
#         numbers = json.load(file)  # 用json.load()載入放在number.json檔裡面的資料，然後將它存到numbers變數中
#         print(numbers["measure_tool"]['number'])

def read_data(file_name):  # 讀取system_data
    file = file_name
    with open(file) as file_origin:
        data = json.load(file_origin)
        return data


def system_data_input_global_var(data):
    pass

#
# system_data = read_data(gvar.system_json)
# system_data_input_global_var(system_data)
# print(system_data)
