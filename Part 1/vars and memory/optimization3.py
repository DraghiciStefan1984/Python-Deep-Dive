import string
import time


def my_func():
    a=24*60
    b=(1,3)*5
    c='abbh'*3
    d='ed'*20
    e='the quick brown fox'*11
    f=['a','b']*3

print(my_func.__code__.co_consts)


def my_func(e):
    if e in [3,4,2,4,2]:
        pass

print(my_func.__code__.co_consts)


char_list=list(string.ascii_letters)
char_tuple=tuple(string.ascii_letters)
char_set=set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


start=time.perf_counter()
membership_test(10000000, char_list)
end=time.perf_counter()
print('for list it took: ', end-start, ' seconds')


start=time.perf_counter()
membership_test(10000000, char_tuple)
end=time.perf_counter()
print('for tuple it took: ', end-start, ' seconds')


start=time.perf_counter()
membership_test(10000000, char_set)
end=time.perf_counter()
print('for set it took: ', end-start, ' seconds')