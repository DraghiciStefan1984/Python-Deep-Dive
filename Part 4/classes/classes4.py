# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:06:14 2020

@author: Stefan Draghici
"""

class Person:
    def hello(arg='default'):
        print(f'hello with arg={arg}')
        
    def instance_hello(self, arg):
        print(f'hello with arg={arg}')
        
    @classmethod
    def class_hello(cls, arg):
        print(f'hello with arg={arg}')

        
#test
Person.hello()
p=Person()
p.hello()



class MyClass:
    def hello():
        print('hello...')
        
    def instance_hello(self):
        print(f'hello with arg={self}')
        
    @classmethod
    def class_hello(cls):
        print(f'hello with arg={cls}')
        
    @staticmethod
    def static_hello():
        print('static hello')

#test
m=MyClass()
MyClass.hello()
#m.hello()
m.instance_hello()
MyClass.class_hello()
m.class_hello()
MyClass.static_hello()
m.static_hello()



from datetime import datetime, timezone, timedelta

class Timer:
    tz=timezone.utc
    
    @classmethod
    def set_tz(cls, offset, name):
        cls.tz=timezone(timedelta(hours=offset), name)
        
    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)
    
    def start(self):
        self._time_start=self.current_dt_utc()
        self._time_end=None
        
    def end(self):
        if self._time_start is None:
            raise TimerError('Must start timer first')
        self._time_end=self.current_dt_utc()
        
    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started.')
        return self._time_start.astimezone(self.tz)
    
    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not ended.')
        return self._time_end.astimezone(self.tz)
    
    
class TimerError(Exception):
    """Custom exception for Timer class"""
    pass
    
#test
t1=Timer()
t2=Timer()
Timer.set_tz(-8, 'PST')
print(t1.tz, t2.tz)
print(Timer.current_dt_utc())
print(t1.current_dt_utc())


