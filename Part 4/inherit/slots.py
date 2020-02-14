# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:51:44 2020

@author: Stefan Draghici
"""

class Location:
    __slots__='name', '_longitude', '_latitude'
    
    def __init__(self, name, longitude, latitude):
        self._name=name
        self._longitude=longitude
        self._latitude=latitude
        
    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude