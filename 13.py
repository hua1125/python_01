class all():
    a = {'role': 'admin', 'account': 'root', 'password': '123456', 'dep': 'admin'}
    b = {'role': 'user', 'account': 'hua', 'password': '456789', 'dep': 'user'}
    f = open('data.txt', 'w+')
    f.write(str(a))
    f.write(str(b))
    c=[]
    for line in f.readline():
        line = line.strip('\n')
        n = line.split(' ')
        c.append(n)
    c=dict(c)
    f.close()
    try:
        f = open('data.txt', 'a+')
        contents = f.readline()
        for x in contents:
            print(x)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()
    def load(self):
        global d
        d={}
        i=1
        while i<2:
            account = input('请输入账号：')
            password = input('请输入密码：')
            if account==self.a['account'] and password==self.a['password']:
                d.update({'code':'0','message':'登录成功'})
                d.update(self.a)
                print('登录成功')
                break
            elif account==self.b['account'] and password==self.b['password']:
                d.update({'code': '0', 'message': '登录成功'})
                d.update(self.b)
                print('登录成功')
                break
            elif account=='' or password=='':
                print('用户名或密码不能为空请重新输入')
            else:
                print('登录失败')
                d.update({'code': '1', 'message': '登录失败'})
                break
    def inq(self):
        if d['message']=='登录成功':
            account = input('请输入查询的用户名')
            if self.c['account'] == account:
                self.c['password']='*******'
                print(self.c)
            else:
                print('没有此用户')
        elif d['message']=='登录失败':
            print('权限不足')
    def add(self):
        o=1
        while o<2:
            key_word = input('请输入：')
            if key_word=='add':
                role=input('请输入用户角色：')
                account=input('请输入账户：')
                password=input('请输入密码：')
                dep=input('请输入部门：')
                c={'role':role,'account':account,'password':password,'dep':dep}
                f=open('data.txt','a')
                f.write(str(c))
                f.close()
                break
            else:
                print('请重新输入：')

g=all()
# g.load()
# g.inq()
g.load()
# g.add()
g.inq()