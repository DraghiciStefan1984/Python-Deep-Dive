def squares(n):
    for i in range(n):
        yield i**2
        
def delegator(n):
    # for value in squares(n):
        # yield value
    yield from squares(n)
        
gen=delegator(10)
for _ in range(5):
    print(next(gen))
    
    
def echo():
    while True:
        received=yield
        print(received[::-1])
        
def delegator():
    e=echo()
    yield from e
    
d=delegator()
next(d)
print(d.send('stressed'))