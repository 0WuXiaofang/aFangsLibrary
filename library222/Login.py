from easygui import *
def login(lista):
    # 登录，验证用户输入的信息
    user_info = []
    user_info = multpasswordbox(msg='请输入登录信息', title='Login', fields=('用户名', '密码'))
    name = user_info[0]
    password = user_info[1]
    if name in lista.keys():
        targp = lista[name]
        if targp == password:
            return (1)
        else:
            login(lista)
    else:
        msgbox("该用户不存在或账户错误，请重新输入")
        login(lista)
