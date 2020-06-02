class Callable1:
    def __init__(self, x=0):
        print('callable class')
        self.x=x

c1=Callable1()
c2=Callable1()
print()

class Callable2:
    def __init__(self, x=0):
        print('callable class')
        self.x=x

    def __call__(self):
        print('updating counter')
        self.x+=1

c1=Callable2()
c2=Callable2()
Callable2.__call__(c1)
Callable2.__call__(c2)
print(c1.x)
print(c2.x)