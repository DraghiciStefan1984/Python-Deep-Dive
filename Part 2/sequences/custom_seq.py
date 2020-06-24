class CustomSequence:
    def __init__(self, n):
        self.n=n
    
    def __len__(self):
        print('called __len__')
        return 'test'

    def __getitem__(self, value):
        if value>=self.n:
            raise IndexError
        print(f'you requestetd {value}')
        return 'requested elem'


from functools import lru_cache

class Fib:
    def __init__(self, n):
        self.n=n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s<0:
                s=self.n+s
            if s<0 or s>=self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            start, stop, step=s.indices(self.n)
            rng=range(start, stop, step)
            return [Fib._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2*10)
    def _fib(n):
        return 1 if n<2 else Fib._fib(n-1)+Fib._fib(n-2)


f=Fib(8)
print(f[0])
print(f[1])
print(f[2])
print(f[3])
    