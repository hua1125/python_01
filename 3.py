#1.输入a,b,c,d4个整数，计算a+b-c*d的结果
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(a+b-c*d)


#2.打印1~100内被3整除的所有数的和
e=0
for i in range(101):
    if i%3==0:
        e+=i
print(e)

#3.使用range()输出1~10内的所有奇数 。
for q in range(11):
    if q%2!=0:
        print(q)

#4.打印1~100所有偶数的和 减去 所有奇数的和 的值
r=0
t=0
for e in range(101):
    if e%2==0:
        r+=e
    else:t+=e
print(r-t)




