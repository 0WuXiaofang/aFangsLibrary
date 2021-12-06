from easygui import *
import pymysql
def return_book():
    '''归还图书，如在借表中，借表该书数目减一，图书表书目加一，反之返回不存在'''
    borrow_msg = []
    borrow_msg = multenterbox("还书", "图书借阅系统", ["id"])
    # 连接database
    conn = pymysql.Connect(
        host='localhost',  # 数据库ip地址
        port=3306,  # 端口号
        user='a Fang',  # 用户名
        passwd='123456',  # 密码
        db='2020.11.10',  # 数据库名称
        charset='utf8'
    )

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    sql1 = "SELECT * FROM allbook WHERE id='%d'" % (int(borrow_msg[0]))
    cursor.execute(sql1)
    result = cursor.fetchone()

    # print("您要归还的书籍书名：%s 作者：%s 当前剩余：%d本 还后：%d本" % (result[1], result[2], result[3],result[3]+1))
    # 如果在表中则对已有的图书amount进行更新
    if result:
        sql = "UPDATE allbook SET amount=amount+%d WHERE id='%s'" % (1, borrow_msg[0])
        cursor.execute(sql)
        # 涉及写操作要注意提交
        conn.commit()
        sql1 = "UPDATE borrowtable SET amount=amount-%d WHERE id='%s'" % (1, borrow_msg[0])
        cursor.execute(sql1)
        # 提交
        conn.commit()
    # 未找到书直接返回未找到
    else:
        print("没有该书")
    # 关闭数据库连接
    conn.close()
    return
