# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 07:58:36 2019

@author: Stefan Draghici
"""

my_list=[1,2,3]
print(hex(id(my_list)))

my_list.append(4)
print(hex(id(my_list)))

my_list_1=[1,2,3]
print(hex(id(my_list_1)))
my_list_1=my_list_1+[4]
print(hex(id(my_list_1)))

my_dict=dict(key1=1, key2='a')
print(hex(id(my_dict)))
my_dict['key3']=4.5
print(hex(id(my_dict)))

my_tuple_1=(1,2,3)
print(hex(id(my_tuple_1)))
my_tuple_2=([1,2], [3,4])
print(my_tuple_2)
print(hex(id(my_tuple_2)))
my_tuple_2[0].append(3)
print(my_tuple_2)
print(hex(id(my_tuple_2)))

def process(s):
    print('initial s#={0}'.format(hex(id(s))))
    s+=' word'
    print('final s#={0}'.format(hex(id(s))))
          
my_var='hello'
print('my_var s#={0}'.format(hex(id(my_var))))
process(my_var)
print('my_var s#={0}'.format(hex(id(my_var))))
      
def modify_list(l):
    print('initial l#={0}'.format(hex(id(l))))
    l.append(5)
    print('final l#={0}'.format(hex(id(l))))
          
my_list=[1,2,3,4]
print('my_list l#={0}'.format(hex(id(my_list))))
modify_list(my_list)
print('my_list l#={0}'.format(hex(id(my_list))))
      
def modify_tuple(t):
    print('initial t#={0}'.format(hex(id(t))))
    t[0].append(5)
    print('final t#={0}'.format(hex(id(t))))
          
my_tuple=([1,2,3,4], 'a', False)
print('my_tuple t#={0}'.format(hex(id(my_tuple))))
modify_tuple(my_tuple)
print('my_tuple t#={0}'.format(hex(id(my_tuple))))