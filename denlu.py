# ## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
def load():
    a={'role':'admin','account':'root','password':'123456','dep':'admin'}
    b={'role':'user','account':'hua','password':'456789','dep':'user'}
    global d
    d={}

    i=1
    while i<2:
        account = input('请输入账号：')
        password = input('请输入密码：')
        if account==a['account'] and password==a['password']:
            d.update({'code':'0','message':'登录成功'})
            d.update(a)
            print('登录成功')
            break
        elif account==b['account'] and password==b['password']:
            d.update({'code': '0', 'message': '登录成功'})
            d.update(b)
            print('登录成功')
            break
        elif account=='':
            print('用户名不能为空请重新输入')
            account = input('请输入账号：')
            password = input('请输入密码：')
        elif password=='':
            print('密码不能为空请重新输入')
        else:
            print('登录失败，请重新输入')
            d.update({'code': '1', 'message': '登录失败'})
            break
load()


def inq():
    if d['message']=='登录成功':
        account = input('请输入查询的用户名')
        if d['account'] == account:
            d['password']='*******'
            print(d)
        else:
            print('没有此用户')
    elif d['message']=='登录失败':
        print('权限不足')

inq()