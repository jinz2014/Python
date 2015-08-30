def args(*args, **kwargs):
  print(args)
  print(kwargs)
  for i in args:
    print(i)


# a dic
print("args({'a':1, 'b':2})")
args({'a':1, 'b':2})

# just keyword args, nothing to do with dict
print("\nargs(a=1, b=2)")
args(a=1, b=2)

# sequence
print("\nargs('a1b2')")
args('a1b2')

# a tuple with 4 element
print("\nargs('a',1,'b',2)")
args('a',1,'b',2)

# a tuple with 1 element
print("\nargs(('a',1,'b',2))")
args(('a',1,'b',2))
