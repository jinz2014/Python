'''
foo has two variables in its local namespace:  arg and x

the global space has
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': 'test_namespace.py', '__package__': None, '__name__': '__main__', 'foo': <function foo at 0x6ffffe2d668>, '__doc__': None}
'''

def foo(arg):
  x = 1
  print(locals())
  print(globals())

# {'arg' : 7, 'x' : 1}
foo(7)
foo('bar')
