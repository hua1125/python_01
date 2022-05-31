# 需求-迭代2：用户查询功能:
# 1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
# 2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
# 3. 若输入的用户名不正确 ，给出无查询结果的提示
# 4. 查询支持模糊查询。

from denlu  import load

def inq():
    if d['message']=='登录成功':
        account = input('请输入查询的用户名')
        if d['account'] == account:
            d['password']='*******'
            print(d)
        else:
            print('没有此用户')
    else:
        print('权限不足')

inq()
