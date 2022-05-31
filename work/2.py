a=input('请输入：')
b=0
c=0
d=0
e=0
for i in a:
    if i.isalpha()==1:
        b+=1
    elif i.isdigit()==1:
        c+=1
    elif i.isspace()==1:
        d+=1
    else: e+=1
print(b,c,d,e)