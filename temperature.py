#end='' not supported in P2.7

def convert_to_celsius(f):
  """
  (number) -> float
  """
  return (f-32)*5/9;



if __name__ == '__main__':
  print('80, 78.8 and 10.4 degrees F are equal to ', end='')
  print(convert_to_celsius(80), end=', \n')
  print(convert_to_celsius(78.8), end=', and ')
  print(convert_to_celsius(10.4), end=' Celsius')
