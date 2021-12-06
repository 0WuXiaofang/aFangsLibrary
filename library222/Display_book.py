import pymysql
def display_book():
    '''连接database'''
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
    # 输出所有的书
    sql = "select book from borrowtable"
    cursor.execute(sql)
    data = cursor.fetchall()
    library_books = []
    for book in data:
        library_books.append(book[0])
    print("全书为", library_books)
    conn.close()
    cursor.close()
    return

