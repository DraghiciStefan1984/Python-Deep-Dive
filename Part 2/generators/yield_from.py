def matrix(n):
    return ((i*j for j in range(1, n+1)) for i in range(1, n+1))


m=list(matrix(10))

file1='car-brands-1.txt'
file2='car-brands-2.txt'
file3='car-brands-3.txt'
files=file1, file2, file3
brands=[]

with open(file1) as f:
    for brand in f:
        brands.append(brand.strip('\n'))


def brands(*files):
    for f_name in files:
        with open(f_name) as f:
            for line in f:
                yield line.strip('\n')