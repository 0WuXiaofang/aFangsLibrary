from easygui import *
import connect
import pymysql
def append_book():
    append_msg = []
    append_msg = multenterbox("添加新书", "图书管理系统", ["id", "书名", "作者", "数目"])
    # 连接database
    connect.connect()
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()

    sql = "SELECT * FROM allbook WHERE book='%s'AND author='%s'" % (append_msg[1], append_msg[2])
    cursor.execute(sql)
    results = cursor.fetchone()
    # 如果在表中则对已有的图书amount进行更新
    if results:
        sql = "UPDATE allbook SET amount=amount+%d WHERE name='%s' AND author='%s'" % (
            int(append_msg[3]), append_msg[1], append_msg[2])
        cursor.execute(sql)
        # 涉及写操作要注意提交

        conn.commit()
    # 如果没有在表中则插入一条图书数据
    else:
        sql = "INSERT INTO allbook VALUES('%d','%s','%s','%d')" % (
            int(append_msg[0]), append_msg[1], append_msg[2], int(append_msg[3]))
        cursor.execute(sql)
        # 提交
        conn.commit()
    conn.close()
