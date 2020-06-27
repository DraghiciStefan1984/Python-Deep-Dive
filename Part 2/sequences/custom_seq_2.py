class CustSeq:
    def __init__(self, name):
        self.name=name

    def __repr__(self):
        return f'CustSeq(name={self.name})'

    def __add__(self, other):
        return CustSeq(self.name+other.name)

    def __iadd__(self, other):
        if isinstance(other, CustSeq):
            self.name+=other.name
        else:
            self.name+=other
        return self

    def __mul__(self, n):
        return CustSeq(self.name*n)

    def __rmul__(self, n):
        return CustSeq(self.name*n)

    def __imul__(self, n):
        self.name*=n
        return self

    def __contains__(self, value):
        return value in self.name


c1=CustSeq('cust 1')
c2=CustSeq('cust 2')

res=c1+c2
print(res)

c1+=c2
print(c1)

res=c1*8
print(res)

print('c' in c1)