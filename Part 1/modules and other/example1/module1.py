# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:19:39 2020

@author: Stefan Draghici
"""

print('*************** Running {} ***************'.format(__name__))

def pprint_dict(header, d):
    print('\n\n--------------------------')
    print('******{}******'.format(header))
    for key, value in d.items():
        print(key, value)
    print('--------------------------\n\n')
    
pprint_dict('module1.globals', globals)

print('*************** End of {} ***************'.format(__name__))