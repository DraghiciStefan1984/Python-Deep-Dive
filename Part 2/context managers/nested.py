with open('file1.txt') as f1:
    with open('file2.txt') as f2:
        with open('file3.txt') as f3:
            print(f1.readlines())
            print(f2.readlines())
            print(f3.readlines())


from contextlib import contextmanager

@contextmanager
def open_file(f_name):
    print(f'opening {f_name}')
    f=open(f_name)
    try:
        yield f
    finally:
        print(f'closing {f_name}')
        f.close()