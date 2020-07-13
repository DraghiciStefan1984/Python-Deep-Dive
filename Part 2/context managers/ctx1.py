try:
    print(10/2)
except ZeroDivisionError:
    print('zero div ex occured')
finally:
    print('this will always run')


with open('test.txt', 'w') as file:
    print('inside with: file closed?', file.closed)


with open('test2.txt', 'w') as f:
    f.writelines('this is a test')

with open('test2.txt') as f:
    row=next(f)
    print(row)