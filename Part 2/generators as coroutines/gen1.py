def averager():
    total=0
    count=0
    def inner(value):
        nonlocal total
        nonlocal count
        total+=value
        count+=1
        return total/count
    return inner


def running_averager(iterable):
    avg=averager()
    for value in iterable:
        running_average=avg(value)
        print(running_average)

running_averager([1,2,3,4])


def running_averager_cor():
    total=0
    count=0
    running_average=None
    while True:
        value=yield running_average
        total+=value
        count+=1
        running_average=total/count
