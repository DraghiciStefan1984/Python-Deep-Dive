import enum


class Color(enum.Enum):
    red=1
    green=2
    blue=3
    

class Status(enum.Enum):
    PENDING='pending'
    RUNNING='running'
    COMPLETED='completed'
    
    
class NumSides(enum.Enum):
    triangle=3
    rectangle=4
    square=4
    rhombus=4
    
print(NumSides.rectangle is NumSides.rhombus)


# this will raise a duplicate error
@enum.unique
class Status(enum.Enum):
    ready=1
    done_ok=2
    errors=3
    waiting=1