s = "India is my country"

s.startswith("India")
# => True

s.endswith("country")
# => True

s.find("my")
# => 9

s.find("xx")
# => -1

s.index("country")
# => 12

s.index("xx")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found

# s.index("hello")
# => Traceback (most recent call last):
#  	 File "<stdin>", line 1, in <module>
#    ValueError: substring not found

" India ".strip()
# => "India"

