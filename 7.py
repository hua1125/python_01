def add(x,y):
    z=x+y
    return z

for q in range(10):
    for w in range(10):
        print(add(q,w))


print(add(str(4),'wl'))
print(add('ddd',str(5)))

def ll(r,t):
    j='{}年级上{}课'.format(r,t)
    return  j
print(ll(t=1,r='yuwen'))