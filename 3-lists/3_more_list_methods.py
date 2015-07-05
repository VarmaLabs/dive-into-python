fruits = ["mangoes", "grapes", "banana"]
print(fruits)

fruits.index("mangoes")
# => 0

fruits.index("banana")
# => 2

fruits.count("mangoes")
# => 1
fruits.count("apples")
# => 0

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.pop()
# => "banana"
print(fruits)
