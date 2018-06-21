# Class Week 2
# June 19, 2018
# IS 590 PRO

# Default values for a function

def print_again(string, number_of_reps=2):
    return print(string * number_of_reps)

# This will override the default value of 'number_of_reps'
print_again('Hurray', number_of_reps=5)

# Docstrings
# Enclosed in triple double-quotes
# Right below the definition line of a function is the most common place for them
# We can also put them at the top of a Python script
# First line is general description
#   then :param describes each part

# def Function():
#       :param n: an integer
# This is one basic example of what it'd look like

# You can have functions that return more than one data type:
#   def fun(x):
#       if x > 5:
#           return 'something'
#       else:
#           return 55
#
# This will either return a string or an int

# Creating doc string: Type out full function, then your three double quotes and Enter,
#   and Python will help fill it out for you

def fun(x):
    """have some fun.

    :param x: a determinant number
    :return:
    """
    if x > 5:
        return 'something'
    else:
        return 'something else'

y = fun(10)

# If you're writing something, for example, that's very security-sensitive, you might want to
#   force type checking in Python

#   if not isintance(string, str):
#       raise ValueError('parameter "string" should be a str type (or a subclass).')

# This is often not necessary and often takes away the Python flexibility

# To install this module we will need for assignment 3: click on Termimal on the bottom
# 'pip install pygeodesy'
# It took a minute, but then it downloaded and said it successfully installed the package

import pygeodesy

# This is a special purpose geographic data calculation package
# We haven't yet used the latitude and longitude
# One of the challenges of A.3 is to calculate distances traveled, etc. of the storms

from pygeodesy import ellipsoidalVincenty as ev
a = ev.LatLon('0.0N', '0.0W')
b = ev.LatLon('1.0N', '0.0W')
c = ev.LatLon('0.0N', '1.0W')
d = ev.LatLon('1.0N', '1.0W')

# Do some sanity checks:
print(a.distanceTo3(b))     # This is moving straight North, 0 degrees
print(a.distanceTo3(c))

z = ev.LatLon('15.0N', '59.0W')
w = ev.LatLon('16.0N', '60.0W')

# Then convert distance in meters to nautical miles

meters = z.distanceTo(w)
distance = meters / 1852.0
bearing = a.bearingTo(w)
knots = distance / 6        # We can't hardcode this 6 (hours) because sometimes the times aren't
                            #   in perfect 6 hour intervals
# Relook at the lecture notes that are online in GitHub for more details on these examples


# Anytime a function exits without a return, it will return None !!!!!!


# Lambda functions are used more commonly in Python than in other languages
# Lambda functions are never required to write anything, but they may often appear in
#   other people's code.

# Common during custom sorting functions

list_of_tuples = [(1, 'Joe'),
                  (2, 'James'),
                  (5, 'Smith'),
                  (10, 'Charles'),
                  (3, 'Alberta'),
                  (4, 'Francine'),
                  (2, 'Adam'),
                  (7, 'Charles')]
print(sorted(list_of_tuples))    # This produces the standard sorted order.

def get_name_from_tuple(t: tuple) -> str:
    return t[1]

print(get_name_from_tuple((2, 'Adam')))

print(sorted(list_of_tuples, key=get_name_from_tuple))      # Function that isn't called is the key:
                                                            #   'a callable'
# We can use a function as a data object
# Here, the function provides the kind of sorting that is done

# Lambda function is the shorthand for the above example

print(sorted(list_of_tuples, key=lambda t: t[1]))           # Here's the shorthand. Same output.

# Now how to order the results again? So that it sorts first alphabetically, and then it sorts
#   numerically for when the names match

print(sorted(list_of_tuples, key=lambda t: (t[1], t[0])))       #This sorts both ways.

# If you only need to sort once in your code, it might not make sense to write out the entire function
#   just to use it once. So that's where lambda functions come in, you can write a very short line
#   and then use it and lose it. As soon as the line of code is done, the lambda function disappears
#   from memory. That's why you can have lambda function after lambda function in different statements,
#   and they won't interfere with each other.


# This does not immediately get rid of the lambda function, because it is no longer anonymous,
#   as it now is assigning a return value to the lambda function:
triple = lambda x: x * 3

print(triple(5))
print(triple(40))

# First Class Functions & Closures
#
# In Python, all functions are objects, this is called first class functions
#
# The Lambda function is kind of like a function that returns a functions

def multiplier_creator(n: int):
    new_function = lambda x: print(x, 'times', n, 'is', x * n)
    return new_function


# Same as:
#       return lambda x: print(x, 'times', n, 'is', x * n)

# Same as:
#       def multiplier_creator(n: int):
#           def new_function(x):
#               print(x, 'times', n, 'is', x * n)
#           return new_function

doubler = multiplier_creator(2)
tripler = multiplier_creator(3)
quadrupler = multiplier_creator(4)

doubler(10)
tripler(9)
quadrupler(4)

quadrupler(4000)

# This sort of violates the scope rules, because the variable 'n' only exists in the outer function,
#   and is not passed directly to the inner function. Also 'x' is passed from function call to the
#   inner function and is *seemingly* not passed to the outer function.

#   else:
#       raise ValueError('operation parameter was invalid/: ', operation)
#   This is how to add a custom message to an error


