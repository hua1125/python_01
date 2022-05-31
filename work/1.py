#辅助指令 m。n
my_str3='一斤苹果%2.3f元' %3.2
print(my_str3)
#显示左对齐 -
my_str4='一斤苹果%-12.1f元' %3.2
print(my_str4)
#在数字前面显示+
my_str5='一斤苹果%+2.3f元' %3.2
print(my_str5)
#在前面显示 0
my_str6='一斤苹果%012.3f元' %3.2
print(my_str6)

#使用Format格式化，{}.format('字符串')
my_str8='张三今年{}岁'.format(25)
print(my_str8)
#format格式化两个参数:{} {} .format(参数1，参数2)
my_str9='{}今年{}岁'.format('张三',25)
print(my_str9)
#1连接字符串：join
a='hello'
b=a.join('world')
print(b)
#2分割字符串 split
c=a.split('e')
print(c)
#查找字符串 find
q='nfjnjkbhg55463f2'
print(q.find('n'))
#查找以xxx为结尾的字符串：endwith（‘xxx’）
fstr='测试报告.doc'
if fstr.endswith('doc'):
    print('haol')

#替换字符串：replace(old_value,new_value)
gstr='hello world'
t=gstr.replace('world','python')
print(t)
