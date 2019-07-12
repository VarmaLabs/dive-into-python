fruits = ["mango", "grapes"]
print id(fruits)

fruits.append("banana")
print id(fruits)

a = 1
print id(a)

a = a + 1
print id(a)

# a is a variable which points to 
# memory location 700 which has a value 1

# a ---> 700

# a + 1 is calculated and is stored
# in the memory location 800

# a + 1 ----> 800

# a is pointed to 800 (as a is a + 1)
# a ----> 800

# Memory location 700 gets garbage collected


