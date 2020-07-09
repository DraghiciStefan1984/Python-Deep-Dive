gen_expression=(i**2 for i in range(100))

print(next(gen_expression))
print(next(gen_expression))
print(next(gen_expression))
print(next(gen_expression))

start=1
stop=10

mult_list=[[i*j for j in range(start, stop+1)] for i in range(start, stop+1)]
print(mult_list)

mult_gen=((i*j for j in range(start, stop+1)) for i in range(start, stop+1))
print([list(row) for row in mult_gen])

mult_gen_2=([i*j for j in range(start, stop+1)] for i in range(start, stop+1))
print([i for i in mult_gen_2])


from math import factorial

def combo(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

size=10
pascal=[[combo(n, k) for k in range(n+1)] for n in range(size+1)]
print(pascal)