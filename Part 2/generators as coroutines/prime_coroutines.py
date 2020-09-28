def coroutine(gen_fn):
    def inner():
        gen=gen_fn()
        next(gen)
        return gen
    return inner


@coroutine
def echo():
    while True:
        received=yield
        print(received)
        
        
e=echo()
e.send('hello')