class Averager:
    def __init__(self):
        self.numbers=[]

    def add(self, number):
        self.numbers.append(number)
        total=sum(self.numbers)
        count=len(self.numbers)
        return total/count


a=Averager()
a.add(10)
a.add(20)
print(a.add(30))


def averager():
    numbers=[]
    def add(number):
        numbers.append(number)
        total=sum(numbers)
        count=len(numbers)
        return total/count
    return add

a=averager()
a(10)
a(20)
print(a(30))


def averager():
    total=0
    count=0
    def add(number):
        nonlocal total
        nonlocal count
        total+=number
        count+=1
        return total/count
    return add