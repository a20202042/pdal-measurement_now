import base64
import MySQLdb, os, re
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class sql_connect:
    def __init__(self):
        self.sql_host = '163.18.69.14'
        self.sqldb = 'pdal-measurement'
        self.sql_user = 'root'
        self.sql_charset ='utf8'
        self.sql_password = "rsa+0414018"
        self.conn = MySQLdb.connect(host=self.sql_host, user=self.sql_user, passwd=self.sql_password, db=self.sqldb,
                                    charset=self.sql_charset)# 新增 charset="utf8"才會顯示中文
        self.cursor = self.conn.cursor()
    def sql_image_all_project_name(self):#取所有資料:量具、專案名稱
        SQL = ("SELECT mysite_project.project_name "
               " From  mysite_project")
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        new_data = []
        for item in data:
            item = list(item)
            new_data.append(item[0])
        print(new_data)
        return new_data

    def sql_image_base64data(self, item_name): #已量測部位抓取
        SQL = ("SELECT mysite_measure_items.image_base64_data "
               " From  mysite_measure_items"
               " WHERE mysite_measure_items.measurement_items ='%s'"%item_name)
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        data = data[0][0]
        return data

    def sql_all_image_item(self,project_name):#取所有資料:量具、專案名稱
        SQL = ("SELECT mysite_measure_items.measurement_items "
               " From  mysite_measure_items"
               " WHERE mysite_measure_items.project_measure_id"
               "=(SELECT mysite_project.id FROM mysite_project WHERE mysite_project.project_name='%s')" % project_name)
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        new_data = []
        for item in data:
            d = item[0]
            new_data.append(d)
        print(new_data)
        return new_data

# img_path = ('D:/GitHub/pythonProject/NOGO.PNG')
#
# def open_file():
#     with open(img_path, 'rb') as file:
#         image_data = file.read()
#         base64_data = base64.b64encode(image_data)  # base64編碼
#         print(str(base64_data, 'utf-8'))  # 去掉"b

def save(file_name, base64_data, pict_type):
    with open('%s.%s' % (file_name, pict_type), 'wb') as file:  # wd 寫入覆蓋文件
        jiema = base64.b64decode(base64_data)  # 解碼
        file.write(jiema)  # 將解碼資料寫入到片圖中
        print(type(jiema))

s = sql_connect()
measure_project = s.sql_image_all_project_name()
for name in measure_project:
    measure_item = s.sql_all_image_item("%s"% name)
    print(measure_item)
    os.makedirs(BASE_DIR + "\\measure_item_image\\%s"%name)
    for item in measure_item:
        data = s.sql_image_base64data(item)
        save("measure_item_image/%s/%s" %(name, item), data, "jpg")


# -------------------------
# 測試寫入
# data = s.sql_all_date("外徑")
# print(data)
# save("measure_item_image/test5", data, 'jpg')
# ---------------------------
# s.sql_all("外徑")
# a= "measure_item/washer 測試/98352597_276690960040261_7159454828798672896_n_OK2cXQ5.jpg"
# list = re.split(r"\d", a)
# print(list[-1])