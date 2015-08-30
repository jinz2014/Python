def memo(f):
  m = {}
  def help(x):
    if type(x) == int and x >= 0:
      if x not in m:
        m[x] = f(x)
      return m[x]
    else:
      raise Exception("Argument is not an integer")

  return help

@memo
def fib(n):
  if n <= 1:
    return n
  else: 
    return fib(n-1) + fib(n-2)

# the fib function is decorated by the memoize() function
#fib = memo(fib)

for i in range(10, -1, -1):
  print(i, fib(i))
