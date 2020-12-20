import MySQLdb


def sql_test():
    conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measurement",
                           charset="utf8")  # 新增 charset="utf8"才會顯示中文
    cursor = conn.cursor()
    # SQL = ("show create table mysite_project" )查詢欄位名稱
    # SQL = ('SHOW CREATE TABLE mysite_project ')
    # SQL = ("SELECT project_name  FROM mysite_project ")
    # select 資料表欄位名稱 From 資料表 :抓取資料表中資料欄位的資料
    # SQL = ("SELECT id, sor_no, part_no"
    #        " FROM mysite_measurement_work_order_create "
    #        "WHERE part_no ='4' AND id = '1'")
    # 找資料表欄位中有where設定的欄位 有跟資料內容相同並且
    i = 222
    SQL = ("SELECT * "
           " From  mysite_measurement_work_order_create "
           " WHERE mysite_measurement_work_order_create.project"
           "=(SELECT mysite_project.id FROM mysite_project WHERE mysite_project.project_name=%s) " % i)
    # SQL = ("SELECT mysite_project.id FROM mysite_project, mysite_measurement_work_order_create WHERE mysite_project.project_name=%s "%i)
    cursor.execute(SQL)
    print(cursor.fetchall())
    return list(cursor.fetchall())


def sql_insert():
    conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measurement",
                           charset="utf8")
    cursor = conn.cursor()
    SQL = "INSERT INTO mysite_measure_values(measure_value, measure_unit,measure_time,measure_name_id, measure_project_id) VALUE('20','mm','2020-09-06','1','1')"
    cursor.execute(SQL)
    conn.commit()
    print('insert ok')


def sql_inaert_value(value_data):
    conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db='pdal-measurement',
                           charset='utf8')
    cursor = conn.cursor()
    SQL = ("SELECT mysite_measure_items.id "
           " From  mysite_measure_items "
           " WHERE mysite_measure_items.measurement_items = '外徑'")
    cursor.execute(SQL)
    measure_item = list(cursor.fetchone())[0]
    SQL = ("SELECT mysite_project.id  "
           " From  mysite_project "
           " WHERE mysite_project.project_name= '測試專案一'")
    cursor.execute(SQL)
    meaure_project_id = list(cursor.fetchone())[0]
    SQL = (
              "INSERT INTO mysite_measure_values(measure_value, measure_unit,measure_time,measure_name_id, measure_project_id)" \
              " VALUE('%s','%s','%s', '%s','%s')") % (
              value_data[0], value_data[1], value_data[2], measure_item, meaure_project_id)
    cursor.execute(SQL)
    conn.commit()
    print('insert ok')


conn = MySQLdb.connect(host="163.18.69.14", user="root", passwd="rsa+0414018", db="pdal-measurement",
                       charset="utf8")
cursor = conn.cursor()
# SQL = ("SELECT mysite_measure_items.measurement_items "
#        " From  mysite_measure_items"
#        " WHERE mysite_measure_items.project_measure_id"
#        "=(SELECT mysite_project.id FROM mysite_project WHERE mysite_project.project_name='%s')" % 'washer')
project_name = 'test'
SQL = ("SELECT mysite_measure_items.measurement_items "
               " From  mysite_measure_items"
               " WHERE mysite_measure_items.project_measure_id"
               "=ANY(SELECT mysite_project.id FROM mysite_project WHERE mysite_project.project_name='%s')" % project_name)
# SQL = ("SELECT mysite_project.id From mysite_project WHERE mysite_project.project_name='%s'" % project_name)
cursor.execute(SQL)
data = cursor.fetchall()
print(data)