# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:01:30 2020

@author: Stefan Draghici
"""

def validate_integer(arg_name, arg_value, min_value=None, max_value=None, custom_min_message=None, custom_max_message=None):
    if not isinstance(arg_value, int):
        raise TypeError(f'{arg_name} must be an int.')
    if min_value is not None and arg_value<min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_name} cannot be less than {min_value}.')
    if max_value is not None and arg_value>max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f'{arg_name} cannot be greater than {max_value}.')