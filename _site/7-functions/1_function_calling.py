#A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide #better modularity for your application and a high degree of code reusing.

#As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own #functions. These functions are called user-defined functions.

#Syntax

#def functionname( parameters ):
#  "function_docstring"
#   function_suite
#   return [expression]

#By default, parameters have a positional behavior and you need to inform them in the same order that they were #defined.


#Calling a function

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str;
   return;

# Now you can call printme function
printme("I'm first call to user defined function!");
printme("Again second call to the same function");






