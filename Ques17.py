# WAP to create an Ordereddict, delete an element from it and insert it again, then print the output.

from collections import OrderedDict

const = OrderedDict()
const['a'] = 1
const['b'] = 2
const['c'] = 3
const['d'] = 4
print(const)

const.pop('c')
print("After deleting 'c' from the dictionary:", const)

const['c'] = 3
print("After inserting 'c' again in the dictionary:", const)