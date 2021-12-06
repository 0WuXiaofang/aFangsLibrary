from easygui import *
import pymysql
def search_book():
    # 查找书籍
    search_msg = enterbox("输入需找书的id", "图书借阅系统")
    # 在数据库图书表中找到指定的信息
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
    sql = "SELECT * FROM allbook WHERE id='%s'" % (search_msg)
    # 执行sql语句
    cursor.execute(sql)
    res = cursor.fetchone()
    if res:
        print("书名：%s 作者：%s." % (res[1], res[2]))
    else:
        print("没有您所要查询的图书")
    # 关闭数据库连接
    conn.close()
