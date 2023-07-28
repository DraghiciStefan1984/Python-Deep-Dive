t = 1, 2, 5, 'a'
a, b, c, d = t
london = "London", "UK", 9000000
new_york = ("New York", "USA", 8500000)
beijing = "Beijing", "China", 21000000

cities = [london, new_york, beijing]
print([city[2] for city in cities])
print(sum(city[2] for city in cities))