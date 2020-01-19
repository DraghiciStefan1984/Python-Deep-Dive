# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:52:30 2020

@author: Stefan Draghici
"""

from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(arg):
    return '{0}(<i>{1}</i>)'.format(arg, str(hex(arg)))

def html_real(arg):
    return '{0:.2f}'.format(round(arg, 2))

def html_str(arg):
    return html_escape(arg).replace('\n', '<br/>\n')

def html_list(arg):
    items=('<li>{0}</li>'.format(html_escape(item)) for item in arg)
    return '<ul>\n'+'\n'.join(items)+'\n</ul>'