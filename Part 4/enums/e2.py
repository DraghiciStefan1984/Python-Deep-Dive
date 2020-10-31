from enum import Enum


class Color(Enum):
    red=1
    green=2
    blue=3
    
    def purecolor(self, value):
        return {self: value}
    
    def __repr__(self):
        return f'{self.name} ({self.value})'
    
print(Color.red.purecolor(100))


class Number(Enum):
    ONE=1
    TWO=2
    THREE=3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value<other.value

print(Number.ONE<Number.TWO)


class Phase(Enum):
    READY='ready'
    RUNNING='running'
    FINISHED='finished'
    
    def __str__(self):
        return self.value
    
    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value==other
        return False
    
    def __lt__(self, other):
        ordered_items=list(Phase.READY, Phase.RUNNING, Phase.FINISHED)
        self_order_index=ordered_items.index(self)
        
        if isinstance(other, Phase):
            other_order_index=ordered_items.index(other)
            return self_order_index<other_order_index