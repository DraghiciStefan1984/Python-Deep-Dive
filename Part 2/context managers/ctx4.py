def my_gen():
    try:
        print('creating context and yielding object')
        yield [1,2,3,4]
    finally:
        print('exiting context and cleanup')


class GenCtxManager:
    def __init__(self, gen_func):
        self._gen=gen_func()

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, ex_type, ex_value, ex_traceback):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False