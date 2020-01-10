# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:13:27 2020

@author: Stefan Draghici
"""

my_list=[1,2,3]
print(id(my_list))
my_list.append(4)
print(id(my_list))

my_dict={'unu':1}
print(id(my_dict))
my_dict['doi']=2
print(id(my_dict))

my_tuple=([4,6],[5,1])
print(id(my_tuple))
my_tuple[0].append(3)
print(id(my_tuple))


def process(s):
    print('initial s#={}'.format(id(s)))
    s=s+'world'
    print('final s#={}'.format(id(s)))
          
process('hello')