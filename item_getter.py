def itemgetter(*items):
  if len(items) == 1:
    item = items[0]
    def g(obj):
      return obj[item]
  else:
    def g(obj):
      return tuple(obj[item] for item in items)
  return g


assert itemgetter(1)('ABCDEFG') == 'B'
assert itemgetter(1,3,5)('ABCDEFG') == ('B', 'D', 'F')
#>>> itemgetter(slice(2,None))('ABCDEFG')
#'CDEFG'

getcount = itemgetter(1)
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
assert map(getcount, inventory) == [3, 2, 5, 1]
assert sorted(inventory, key=getcount) == [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]



# dict[0] is not supported.
#inventory = [{'apple': 3}, {'banana', 2}, {'pear', 5}, {'orange', 1}]
#print( map(getcount, inventory) )
#print(sorted(inventory, key=getcount)) 

