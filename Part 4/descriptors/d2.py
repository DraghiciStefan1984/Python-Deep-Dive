from datetime import datetime


class TimeUTC:
    def __get__(self, instance, owner_class):
        print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
        return datetime.utcnow().isoformat()
    
    
class Logger1:
    current_time=TimeUTC()
    
    
class Logger2:
    current_time=TimeUTC()
    

Logger1.current_time
Logger2.current_time


class Countdown:
    def __init__(self, start):
        self.start=start+1
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        self.start+=1
        return self.start
    
    
class Rocket:
    countdown=Countdown(10)
    
    
r1=Rocket()
r2=Rocket()
print(r1.countdown)
print(r2.countdown)


class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')
        
    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner={owner_class}')
            
            
class Point2D:
    x=IntegerValue()
    y=IntegerValue()
    
    
Point2D.x
p=Point2D()
p.x