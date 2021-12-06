from easygui import *
import pymysql
def delete_book():
    '''删除booktable中指定的全部书籍'''
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
    sql = "select book from allbook"
    cursor.execute(sql)
    data = cursor.fetchall()
    books = []
    for book in data:
        books.append(book[0])
    print("借书列表为", books)
    # 删除书籍
    while True:
        de_book = choicebox(msg='请选择要删除的书', title='图书管理系统', choices=books)
        print("hhhhhhh", de_book, type(de_book))
        sql1 = "SELECT * FROM allbook WHERE book='%s'" % de_book
        cursor.execute(sql1)
        result = cursor.fetchone()
        if result:
            # 如果在表中则对已有的图书进行修改
            # SQL 删除语句
            sql2 = "DELETE FROM allboook WHERE book='%s'" % (de_book)
            try:
                # 执行SQL语句
                cursor.execute(sql2)
                # 提交修改
                conn.commit()
            except:
                # 发生错误时回滚
                conn.rollback()
            finally:
                # 最终关闭数据库连接
                conn.close()
            break
        # 未找到书直接返回未找到
        else:
            print("没有你要删除的书")
            continue