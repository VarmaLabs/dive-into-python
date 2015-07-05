#The Anonymous Functions

#These functions are called anonymous because they are not declared in the standard manner #by using the def keyword. You can use the lambda keyword to create small anonymous #functions.

#Syntax

#The syntax of lambda functions contains only a single statement, which is as follows

#lambda [arg1 [,arg2,.....argn]]:expression

#Following is the example to show how lambda form of function works



# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

 

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )