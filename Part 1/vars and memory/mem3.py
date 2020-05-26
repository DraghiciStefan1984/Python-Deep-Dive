l=[1,2,3]
print(hex(id(l)))

l.append(4)
print(hex(id(l)))

l+=[5]
print(l)

t=(1,2,3)
print(hex(id(t)))

t=([1,2], [3,4])
print(hex(id(t)))

t[0].append(3)
print(t)
print(hex(id(t)))


def process(s):
    print('initial s #={}'.format(hex(id(s))))
    s+=' world'
    print('final s #={}'.format(hex(id(s))))

process('test')


def modify_list(l):
    print('initial s #={}'.format(hex(id(l))))
    l.append(100)
    print('final s #={}'.format(hex(id(l))))

modify_list([1,2,3])