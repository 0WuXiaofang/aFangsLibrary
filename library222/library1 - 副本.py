# 图书管理系统
from easygui import *
import pymysql
import Choice
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
# 执行SQL语句
# cursor.execute(sql)
# 关闭光标对象
# cursor.close()
# 关闭数据库连接
conn.close()
cchoices = 0
if __name__ == "__main__":
    msgbox('欢迎进入图书管理系统', 'Library')
    while 1:
        cchoices = buttonbox(msg='选择登陆方式', title='Library', choices=('普通用户', '管理员'))
        if cchoices is None:
            break
        else:
            Choice.choice(cchoices)
