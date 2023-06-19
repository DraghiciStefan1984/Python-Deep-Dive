s = "string"
print(hex(id(s)))
s = s + " hello"
print(hex(id(s)))

t = ([1, 2, 3], 4, "str")
print(t)
print(hex(id(t)))

t[0].append(4)
print(t)
print(hex(id(t)))

t = (1, 2, 3)
t[1] = 4