from inspect import getcallargs

def f(a, b=1, *pos, **named):
  # print(*pos) invald syntax
  pass

print(getcallargs(f, 1, 2, 3))
# {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}

print(getcallargs(f, a=2, x=4))
# {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
