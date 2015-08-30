class ResultList(list):
  def __init__(self, result, *args):
    self.result = result
    super(ResultList, self).__init__(*args) 

class ResultDict(dict):
  def __init__(self, result, *args, **kwargs):
    self.result = result
    super(ResultDict, self).__init__(*args, **kwargs)

if __name__ == '__main__':
  result = 5
  string = 'abc' # sequence: list('abc')
  rl = ResultList(result, string)
  print(rl)
  print(rl.result)

  puple  = (1,2,3) # a container that supports iteration: list((1,2,3))
  rl = ResultList(result, puple)
  print(rl)

  rl = ResultList(result) # no argument: list()
  print(rl)

  # need keyword argument
  d1 = ResultDict(result, one=1, two=2, three=3)
  print(d1)
  d2 = ResultDict(result, {'one':1, 'two':2, 'three':3})
  print(d2)
  d3 = ResultDict(result, [('one',1), ('two',2), ('three',3)])
  print(d3)
  d4 = ResultDict(result, zip(['one', 'two', 'three'], [1, 2, 3]))
  print(d4)
  d5 = ResultDict(result)
  print(d5)

