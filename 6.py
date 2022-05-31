str=input()
resoult={}
for i in str:
    resoult[i]=str.count(i)
print(resoult)



for x in range(1,10):
    for y in range(1,x+1):
        print(y,'*',x,'=',x*y,end=' ')
    print()



a=[1,2,3,4,5]
b=str(a)
for i in b:
    if i.isdigit():
        print(i,end='')