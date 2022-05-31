from datetime import datetime

#方法：从文件里读取数据，返回的是列表形式的数据
def from_file_get_data(file_name):
    f=None
    try:
        f=open(file_name,'r')
        line=f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


#方法：向文件中写入内容，在用户信息的基础上添加
def sava_data(file_name,file_content):
    f=None
    try:
        f=open(file_name,'w')
        f.write(str(file_content))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()








#定义用户默认数据
# user_list = [{'role':'admin','account':'root','password':'123456','dep':'admin'},{'role':'user','account':'hua','password':'456789','dep':'user'}]
#值 if 表达式1 else  表达式2
user_list = []
user_list=user_list if user_list else from_file_get_data(r'E:\Pycharm\python_01\data.txt')

#定义默认返回结果
result = {"code":0,'message':""}

#定义登录功能
def login (username,password):
    #用户名或密码为空
    if username =='':
        result.update({"code":1,'message':"用户名不能为空"})
        return result
    if password == '':
        result.update({"code":1,'message':"密码不能为空"})
        return result
    #登录的情况
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({'message':"登录成功","user_list":user_list})
            return result
    #登录失败
    result.update({"code":1,'message':"请检查您的用户名或密码是否填写正确！"})
    return result
#创建一个类 ，包括新增用户，修改用户，删除用户，查询用户
class User():

    #添加用户的方法
    def add_user(self,username,password='123456',**kwargs):
        user_dict={}
        user_dict['account'] = username
        user_dict['password'] =password
        user_dict.update(**kwargs)
        #将组装的数据添加到用户列表
        user_list.append(user_dict)
        sava_data('data.txt',user_list)
        result.update({'message':'用户添加成功','addtime':datetime.now()})


    #用户查询
    def get_user(self,username):
        #判断用户是否登录成功
        if not result.get('code') :
            result.update({'code':11,'message':'未登录，权限不足'})
            return result
        #登录成功后，输入正确的用户名查询，返回结果（支持模糊查询）
        result.update({'user_list':[]})
        lst=[]  #存放查询结果的列表
        for x in user_list:
            account = x.get('account')
            if username in account:   #支持模糊查询
                x.pop('password')
                lst.append(x)
        if lst:
            result.update({'message':'查询成功','user_list':lst})
            return  result
        #输入错误的用户名
        result.update({'code':12,'message':'无此用户，请重新输入'})
        return result





if __name__ =='__main__':
#给用户选择
    flag=True
    while flag:
        vls = input('1:)进行登录'
                    '\n 2:)进行查询用户'
                    '\n 3:)添加用户'
                    '\n q:) 退出操作'
                    '\n 其他字符：）未知操作'
                    '\n 请输入：')
        #输入未知符号，重新输入
        if vls not in ('1','2','3','q'):
            print('='*30)
            continue
        #进行登录
        if vls == '1':
            username = input('请输入用户名：')
            password = input('请输入密码：')
            login_result=login(username,password)
            print(login_result)
            print('=' * 30)
            continue
        #进行用户查询
        if vls == '2':
            name = input('请输入查询的用户名：')
            user = User()
            get_result=user.get_user(name)
            print(get_result)
            print('='*30)
            continue
        #添加用户
        if vls == '3':
            name = input('请输入添加的用户名：')
            user=User()
            get_result = user.get_user(name)
            if get_result.get('code') == 12:
                password = input('请输入用户密码：')
                role = input('请输入用户角色：')
                dep = input('请输入用户部门：')
                user.add_user(name,password,role=role,dep=dep)
            if get_result.get('code') == 0:
                result.update({'code':13,'message':'用户已存在'})
                print(result)
            print(get_result)
            print('='*30)
         #退出操作
        if vls == 'q':
            flag=False
            print('退出成功')












