# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:12:11 2020

@author: Stefan Draghici
"""

def echo():
    while True:
        receieved=yield
        print('you said: ', receieved)
  

#test
e=echo()
e.send(None)
e.send('salut')