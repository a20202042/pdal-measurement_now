import MySQLdb, base64
class sql_connect:
    def __init__(self):
        self.sql_host = '163.18.69.14'
        self.sqldb = 'pdal-measurement'
        self.sql_user = 'root'
        self.sql_charset ='utf8'
        self.sql_password = "rsa+0414018"

        self.all_name = ["mysite_project", "mysite_measure_items", "mysite_measurement_work_order_create",
                         "mysite_measuring_tool"]
        self.project_item = ["project_name", "project_create_time", "founder_name", "remake"]
        self.project_work_order = ["project_name", "sor_no", "part_no", "number_of_part", "materials",
                                   "manufacturing_machine",
                                   "batch_number", "class", "inspector", "remake"]
        self.measur_tool = ['tool_name', "tool_type", "tool_precision", "tool_test_date"]
        self.measure_item = ["project_name", "tool_name", "measure_items", "upper", "lower", "center", "decimal_piaces"]

        self.conn = MySQLdb.connect(host=self.sql_host, user=self.sql_user, passwd=self.sql_password, db=self.sqldb,
                                        charset=self.sql_charset)  # 新增 charset="utf8"才會顯示中文
        self.cursor = self.conn.cursor()

    def sql_all_date(self,table_name):#取所有資料:量具、專案名稱
        SQL = ("SELECT * FROM  %s" % table_name)
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        list_data = []
        for item in data:
            all_data = list(item)
            all_data.pop(0)
            list_data.append(all_data)
        # if table_name == "mysite_project" :
        #     self.list_data.insert(0,self.project_item)
        # if table_name =="mysite_measuring_tool":
        #     self.list_data.insert(0,self.project_work_order)
        print("%s_all_date:%s" % (table_name, list_data))
        return list_data
    def sql_find_work_order(self, project_name):
        SQL = ("SELECT * "
               " From  mysite_measurement_work_order_create "
               " WHERE mysite_measurement_work_order_create.project_measure_id"
               "=(SELECT mysite_project.id FROM mysite_project WHERE mysite_project.project_name='%s')" % project_name)
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        list_data = []
        for item in data:
            all_data = list(item)
            all_data.pop(0)
            all_data.pop(-1)
            all_data.insert(0, project_name)
            list_data.append(all_data)
        return list_data

    def sql_find_measure_item(self, project_name):
        SQL = ("SELECT mysite_measure_items.measurement_items,mysite_measure_items.upper_limit, mysite_measure_items.lower_limit, mysite_measure_items.specification_center,"
               " mysite_measure_items.decimal_piaces, mysite_measure_items.measure_unit, mysite_measure_items.measure_points, mysite_measure_items.measure_number,"
               " mysite_measure_items.too_name_id "
               " From  mysite_measure_items "
               " WHERE mysite_measure_items.project_measure_id"
               "=(SELECT mysite_project.id FROM mysite_project WHERE mysite_project.project_name='%s')" % project_name)
        self.measure_item = ["量測專案名稱", "量測項目名稱", "量測數值上限", "量測數值下限", "量測數值中心",
                             "量測小數點位數", "量測單位", "量測點數", "量測次數", "量具名稱"]
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        list_data = []
        for item in data:
            data = list(item)
            SQL = ("SELECT mysite_measuring_tool.toolname From  mysite_measuring_tool WHERE mysite_measuring_tool.id = %s" % data[-1])
            self.cursor.execute(SQL)
            tool_name = self.cursor.fetchall()[0][0]
            data.pop(-1) #量具名稱
            data.append(tool_name)
            data.insert(0, project_name)
            list_data.append(data)
        return list_data

    def sql_all_project_data(self,table_name,project_name):#取關於量測專案資料:工單、量測項目
        SQL = ("SELECT * FROM  %s" % table_name)
        self.cursor.execute(SQL)
        date_all=self.cursor.fetchall()
        self.project_date = list()
        for item in date_all:
            if item[1] == project_name:
                self.project_date.append(list(item))
        return self.project_date

    def sql_version(self):
        self.cursor.execute("SELECT VERSION()")
        return self.cursor.fetchone()

    # def sql_insert(self):
    #     try:
    #         SQL = "INSERT INTO mainsite_project(create_time,name ) VALUE ( '19990731','123' )"
    #         self.cursor.execute(SQL)
    #         self.conn.commit()
    #         print('insert ok')
    #     except:
    #         print('Not insert')
    #
    # def test(self):
    #     try:
    #         sql = "INSERT INTO mainsite_values(measure_value, measure_unit, measure_time, measure_name_id) " \
    #               "VALUE {}, {}, {}, {};".format(('123'), ('mm'), ('2020-09-14'), ('1'))
    #         print(sql)
    #     except:
    #         pass
    def sql_insert_value(self,value_data):
        SQL = ("SELECT mysite_measure_items.id "
               " From  mysite_measure_items "
               " WHERE mysite_measure_items.measurement_items = '%s'"%value_data[-4])
        self.cursor.execute(SQL)
        measure_item = list(self.cursor.fetchone())[0]

        SQL = ("SELECT mysite_measure_items.project_measure_id  "
               " From  mysite_measure_items "
               " WHERE mysite_measure_items.measurement_items = '%s'" % value_data[6])
        self.cursor.execute(SQL)
        meaure_project_id = list(self.cursor.fetchone())[0]

        SQL = ("SELECT mysite_measuring_tool.id  "
               " From  mysite_measuring_tool "
               " WHERE mysite_measuring_tool.toolname = '%s'" % value_data[-2])
        self.cursor.execute(SQL)
        measure_tool_name = list(self.cursor.fetchone())[0]
        print(value_data)
        # ['10', 'mm', '2020-10-16  17:44:36', '66.375', '66.400', '3', '17.Length', '1 - 1', 'Mitutoyo CD - 8"AX']
        SQL = ("INSERT INTO mysite_measure_values(measure_value, measure_unit,measure_time,measure_name_id, measure_project_id,measure_man, measure_number)"
               " VALUE('%s','%s','%s','%s','%s','%s','%s')") %(value_data[0], value_data[1], value_data[2], measure_item, meaure_project_id, value_data[-1], value_data[-3] )
        a = self.cursor.execute(SQL)
        print(type(a))
        self.conn.commit()
        a = self.conn
        b = self.cursor
        print('insert ok')

    def sql_delet_data(self):
        SQL = ("DELETE FROM mainsite_project WHERE name ='123'")
        self.cursor.execute(SQL)
        self.conn.commit()
#---------------------------------------------- 圖片下載

    def sql_image_all_project_name(self):#取所有資料:量具、專案名稱
        SQL = ("SELECT mysite_project.project_name "
               " From  mysite_project")
        self.cursor.execute(SQL)
        data = self.cursor.fetchall()
        new_data = []
        for item in data:
            item = list(item)
            new_data.append(item[0])
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
        return new_data

def save(file_name, base64_data, pict_type):
    with open('%s.%s' % (file_name, pict_type), 'wb') as file:  # wd 寫入覆蓋文件
        jiema = base64.b64decode(base64_data)  # 解碼
        file.write(jiema)  # 將解碼資料寫入到片圖中




import tkinter.messagebox as msgbox

try:
    s = sql_connect()
    a = ['10', 'mm', '2020-10-16  17:44:36', '66.375', '66.400', '3', '17.Length', '1 - 1', 'Mitutoyo CD - 8"AX',
         "海笑"]  # s.sql_inaert_value(['10', 'mm', '2020-10-16  15:42:29', '66.375', '66.400', '3', '17.Length - 1', '1 - 1'])
    s.sql_insert_value(a)
except Exception as e:
    msgbox.showerror('ERROR', '{}\n{}'.format(type(e), e))
# all = s.sql_all_date("mysite_measure_values")
# for i in all:
#     for i_2 in i:
#         print(i_2)
# def sql_test(table_name):
#     conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measure",
#                            charset="utf8")  # 新增 charset="utf8"才會顯示中文
#     cursor = conn.cursor()
#     SQL = ("SELECT * FROM  %s" % table_name)
#     cursor.execute(SQL)
#     print(cursor.fetchall())
#     return list(cursor.fetchall())

# conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measure")
# cursor = conn.cursor()
# cursor.execute("SELECT VERSION()")
# print("Database version : %s " % cursor.fetchone())
# cursor.execute("create table mainsite_students(id int ,name varchar(20),class varchar(30),age varchar(10))") #建立資料表名稱 : mainsite_students
# SQL=("SELECT * FROM mainsite_project")
# cursor.execute(SQL)
# print(list(cursor.fetchone()))
# print(list(cursor.fetchone()))
# # print(list(cursor.fetchall()))
# a = list(cursor.fetchall())
# print(list(list(cursor.fetchall())[0]))
# cursor.fetchall()

# conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measure",charset="utf8")  # 新增 charset="utf8"才會顯示中文
# cursor = conn.cursor()
# SQL =("INSERT INTO mainsite_project(id,name,create_time) VALUES ('5','159','20200731')")
# cursor.execute(SQL)
# conn.commit()