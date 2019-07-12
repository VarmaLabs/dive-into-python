prizes = {'Mangoes': 40.00, 'Banana': 12.00, 'Grapes': 60.00}	

# .copy - Returns a shallow copy of dictionary prizes
print(id(prizes))
copy_of_prizes = prizes.copy()
print(id(copy_of_prizes))

# .get - returns value or default if key not in dictionary
prizes.get('Mangoes')
prizes.get('Apple', 120.00)

# .has_key - Returns true if key in dictionary prizes, false otherwise
prizes.has_key('Mangoes')
# => True
prizes.has_key('Apple')
# => False

# .items - Returns a list of prizes's (key, value) tuple pairs
prizes.items()
# => [('Mangoes', 40.0), ('Banana', 12.0), ('Grapes', 60.0)]

# .keys - Returns list of dictionary prizes's keys
prizes.keys()

# .setdefault - Similar to get(), but will set prizes[key]=default if key is not already in prizes
print(prizes)
prizes.setdefault("Apple", 120.00)
print(prizes)

# .update - Adds dictionary dict2's key-values pairs to prizes
prizes_2 = {'Papaya': '14.50', 'Guava': '32.50'}
prizes.update(prizes_2)
print(prizes)
# => {'Mangoes': 40.0, 'Papaya': '14.50', 'Apple': 120.0, 'Grapes': 60.0, 'Guava': '32.50', 'Banana': 12.0}

# .values - Returns list of dictionary prizes's values
prizes.values()
# => [40.0, 12.0, 60.0]

# .clear - Removes all elements of dictionary prizes
prizes.clear()
print(prizes)
# => {}
