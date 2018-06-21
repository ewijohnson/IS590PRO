fruit = ['apple', 'orange', 'banana', 'tomato', 'starfruit', 'tangerine', 'kiwi']
other_fruits = fruit
print(other_fruits)
fruit[4] = 'kumquat'
print(other_fruits)


# here's how to make a deep copy
# but be careful because it only copies one level deep!
other_fruits = fruit.copy()
print(other_fruits)
fruit.remove('tomato')
print(fruit)
print(other_fruits)


a = [1, 2, 3, ['cat', 'dog', 'horse']]
print(a)
b = a.copy()

a.append(4) # add something to list a to see if it shows up in b
a[3][1] = 'giraffe' # modify a part of the nested list as a test

print(a)
print(b)    # the giraffe will be changed here, but the 4 will not
            # this is because deep copies only copy one level deep
            # so the first level will not change in b when changed in a, but the
            #   second level in a (the inner list) will change in both a and b

# here's how to solve that problem:
print('----------------------')
from copy import deepcopy

a = [1, 2, 3, ['cat', 'dog', 'horse']]
print(a)
b = deepcopy(a) # makes a DEEP copy this time

a.append(4)
a[3][1] = 'giraffe'

print(a)
print(b)

print('_______________________________')

deciduous = ('white oak', 'black walnut', 'red maple', 'silver maple', 'cottonwood')
evergreen = ('holly', 'white pine', 'red cedar', 'blue spruce', 'hemlock')
empty_tuple = ()
one_item_tuple = (1, )  # the hanging comma is REQUIRED to make this a tuple
two_item_tuple = (1, 2)

test = (1 + 5) * 3
test_tuple = (1 + 5, ) * 3
print(test)
print(test_tuple)
print(one_item_tuple)
print(type(test))
print(type(one_item_tuple))

# Can slice and stride with tuples
# Can concatenate tuples, will retain sequence

trees = deciduous + evergreen
print(trees)
print(type(trees))

print(tuple(sorted(trees)))     # 'tuple' is needed here, or else it will become a list
                                # the sorted function always returns a list

# the sorted function has a few operators that can be used

print(tuple(sorted(trees, reverse=True)))

print('------------------------')

# If an immutable object is within a mutable object (list a tuple in a list),
# the contents of the tuple can not be changed, but the entire tuple can be replaced
# This will not affect how the rest of the list works (other items can still be changed,
#   replaced, etc.)


test = [1, 'dog', ['a', 'b', 'c'], (5, 6, 7)]
# This will delete the item
del test[3]

print('--------------------------------')

# Dictionaries
favorite_foods = {'Joe': 'pizza',
                  'Bob': 'beer',
                  'Gina': 'spaghetti',
                  'Anita': 'salad'}
favorite_foods['Bob'] = 'steak'
for name in sorted(favorite_foods):     # This sorts it by Key, here by Person name
    print("{}'s favorite food is {}.".format(name, favorite_foods[name]))

# Dict[KEY] will return the Value

# Keys must be immutable! aka Hashable
# You can use tuples as Dict. Keys, but not lists
# Tuple such as: (Customer name, Customer ID)

# How do we sort the above dictionary by food? (value)

favorite_foods['George'] = 'banana'
favorite_foods['Anita'] = 'salad'
favorite_foods['Zelda'] = 'salad'
favorite_foods['Edward'] = 'steak'
favorite_foods['Edward, Jr.'] = 'steak'

print(favorite_foods.keys())
print(favorite_foods.values())

# To invert a dictionary (swap keys and values)
flipped = {}
for k in favorite_foods.keys():
    v = favorite_foods[k]
    if v not in flipped:
        flipped[v] = k
    else:               # This will retain all the keys when they get inverted
                        # This will make sure no data is elimated when values are
                        #   the same, and the dict is then flipped
        flipped[v] += ', ' + k

print(flipped)
for food in sorted(flipped):
    print("{}'s favorite food is {}.".format(flipped[food], food))

# To make all Values as lists can help clarify data (see lecture notes)

# If you make a dictionary into a list, it only converts the keys, and you lose all values
# Or you can flip first, and then you get all the values and lose the keys

# File input/output:


# This opens a new file and prints to it
tree_list = list(trees)

with open('tree_species.txt', 'w') as f:
# The equivalent to: f = open('tree_species.txt', 'w')
    for tree in tree_list:
        print(tree, file=f)
f.close()

with open('tree_species.txt', 'r') as input_file:
    print(type(input_file))
    new_tree_list = input_file.readlines()
    # readlines() scoops every line into a string, storing an item in a list
print(new_tree_list)

# To get around the new line characters that are printed:

with open('tree_species.txt', 'r') as input_file:
    new_tree_list = input_file.read().splitlines(keepends=False)

with open('sorted_tree_species.txt', 'w') as output_file:
    for tree in sorted(new_tree_list):
        print(tree, file=output_file)

print('________________________')
# For Assignment 2:

# Look at lecture notes!

# Load rand number file all at once with readlines and then go through it all at once
# But this could be an issue because the file could be immense
# So we have to do it a different way!

# This part is in the lecture notes:

# with open('random_numbers.txt', 'r') as f:
#     for line in f:
#         values_on_line = line.split()
#         line_total = 0
#
#         for value in values_on_line:
#             try:
#                 n = int(value)
#             except ValueError:
#                 print('Warning')
#                 n = 0
#             line_total += n
#         print(line_total)

# And that will give us one line of output per file
# We can use something SIMILAR to this on the Assignment 2 - it'll be a little more complex though
