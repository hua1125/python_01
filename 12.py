# 需求-迭代3：用户新增功能:
# 1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
# 2. 需要对文件的读写进行异常捕获
# 3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
# 4. 同时进行查询时，也能查询出该用户 。
#
# from denlu  import load


try:
    f = open('data.txt', 'w')
    contents = f.readline()
    for x in contents:
        print(x)
except Exception as e:
    print(e)
finally:
    if f:
        f.close()

def add():
    key_word=input('请输入：')
    if key_word=='add':
        role=input('请输入用户角色：')
        account=input('请输入账户：')
        password=input('请输入密码：')
        dep=input('请输入部门：')
        c={'role':role,'account':account,'password':password,'dep':dep}
        f=open('data.txt','w+')
        f.write(str(c))
        f.close()
    else:
        print('请重新输入：')
add()