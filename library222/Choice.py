from easygui import *
import  Login
import Operate
#初始化
admsg = {'李元': '111', '王二': '222', '张三': '333'}
usermsg = {'小芳': '444', '婷婷': '555', '小辉': '666'}
def choice(cchoices):
    # 用户登录前身份选择
    if (cchoices == '管理员'):
        Login.login(admsg)
        while 1:
            c = choicebox(msg='请选择下列操作', title='管理员系统', choices=['查看借书书单', '添加书籍', '删除书籍', '退出'])
            if c != '退出':
                Operate.operate(c)
            else:
                msgbox("欢迎下次使用")
                break
    elif (cchoices == '普通用户'):
        Login.login(usermsg)
        while 1:
            c = choicebox(msg='请选择下列操作', title='学生操作系统', choices=['借书', '还书', '输入id查书', '查看书单', '退出'])
            if c != '退出':
                Operate.operate(c)
            else:
                msgbox("欢迎下次使用")
                break
    else:
        return 0