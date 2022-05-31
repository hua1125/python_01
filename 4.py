#5. 求1+2+3+...+100的和
q=0
for i in range(101):
    q+=i
print(q)
#6. 判断一个数n能同时被3和5整除
n=int(input())
if n%3==0 and n%5==0:
    print('对了')
else:print('错了')
#7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
q=int(input())
if q in range(1,101):
    print(q)

#8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x=int(input('请输入x'))
y=int(input('请输入y'))
z=int(input('请输入z'))
w=[x,y,z]
w.sort()
print(w)
#9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
score=int(input('请输入分数：'))
if score>=90:
    print('A')
elif score<90 and score>=60:
    print('B')
else:print('C')

