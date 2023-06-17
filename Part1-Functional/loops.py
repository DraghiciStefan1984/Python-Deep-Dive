i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break # breaks out of the loop

print("\n\n\n")

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue # skip to the next iteration of the loop
    print(i)


for i in range(10):
    print(i)


for c in "hello":
    print(c)


for i in [2,3,4,5,3,4,2]:
    print (i)


for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print("multiple of 7 found")
else:
    print("no multiples of 7 found")


a = 0
b = 2

while a < 4:
    print("-------------")
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print("{0} / {1} - division by zero".format(a, b))
        #continue
        break
    finally:
        print("this always executes")
    
    print("main loop")
else:
    print("code executed without a zero division error")