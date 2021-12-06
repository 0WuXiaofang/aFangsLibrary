import pymysql
def connect():
    #连接数据库
    try:
        conn = pymysql.Connect(
            host='localhost',  # 数据库ip地址
            port=3306,  # 端口号
            user='a Fang',  # 用户名
            passwd='123456',  # 密码
            db='2020.11.10',  # 数据库名称
            charset='utf8'
        )
        print("连接成功")
    except  Exception:
        print("连接异常")
